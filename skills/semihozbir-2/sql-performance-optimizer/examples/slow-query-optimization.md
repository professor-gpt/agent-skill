# Example: Slow Query Optimization

## Input

**Database:** PostgreSQL 15  
**Query:**
```sql
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE EXTRACT(YEAR FROM o.order_date) = 2023
  AND c.status = 'active'
ORDER BY o.amount DESC;
```

**Provided schema (simplified):**
- `orders(id INT PK, customer_id INT, order_date DATE, amount DECIMAL)`
- `customers(id INT PK, status VARCHAR)`
- Existing indexes: `idx_orders_customer_id` on `orders(customer_id)`, `idx_customers_status` on `customers(status)`.

**Execution plan (EXPLAIN ANALYZE):**
```text
Sort  (cost=2345.67..2390.12 rows=9876 width=…) (actual time=120.5..122.1 rows=4500 loops=1)
  Sort Key: o.amount DESC
  Sort Method: external merge  Disk: 1232kB
  ->  Hash Join  (cost=145.32..1956.78 rows=9876 width=…) (actual time=5.1..112.3 rows=4500 loops=1)
        Hash Cond: (o.customer_id = c.id)
        ->  Seq Scan on orders o  (cost=0.00..1789.00 rows=50000 width=…) (actual time=0.01..42.5 rows=50000 loops=1)
              Filter: (EXTRACT(year FROM order_date) = 2023)
              Rows Removed by Filter: 150000
        ->  Hash  (cost=144.50..144.50 rows=98 width=…) (actual time=0.03..0.03 rows=100 loops=1)
              Buckets: 1024  Batches: 1  Memory Usage: 9kB
              ->  Seq Scan on customers c  (cost=0.00..144.50 rows=98 width=…) (actual time=0.01..0.02 rows=100 loops=1)
                    Filter: (status = 'active')
                    Rows Removed by Filter: 9900
```

---

## Analysis

**Bottlenecks:**
1. **`EXTRACT(YEAR FROM order_date) = 2023`** – The function disables index usage on `order_date`. A simple `BETWEEN` would be sargable.
2. **`SELECT *`** – Unnecessary columns increase I/O and may block index‑only scans.
3. **No index on `order_date`** – The orders table is sequentially scanned even though only 2023 rows are needed.
4. **Large sort spill to disk** – ORDER BY `amount DESC` causes a disk sort; an index on `amount` would speed it.

**Execution plan explanation (plain language):**
- The database first scans the entire `orders` table (200,000 rows) and evaluates the `EXTRACT` filter for each row, discarding 150,000 rows.
- It does a similar full scan on `customers` but only 10,000 rows — still, only 100 active customers found.
- Those results are joined using a hash table in memory.
- Finally, the 4,500 joined rows are sorted by `amount` descending, but the sort needed temporary disk space because it was too large for memory.

---

## Optimized Query

```sql
SELECT o.id, o.customer_id, o.order_date, o.amount,
       c.id AS customer_id, c.status
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date BETWEEN '2023-01-01' AND '2023-12-31'
  AND c.status = 'active'
ORDER BY o.amount DESC;
```

**Changes:**
- Replaced `EXTRACT` with a `BETWEEN` range (sargable).
- Enumerated needed columns instead of `SELECT *`.
- If `orders.amount` is often sorted, an index can help (see recommendations).

---

## Index Recommendations

1. **Covering index for the date filter and sort:**
   ```sql
   CREATE INDEX idx_orders_date_amount ON orders(order_date, amount DESC);
   ```
   This allows an index‑only scan for the WHERE clause and returns rows already sorted by `amount DESC`, eliminating the sort.

2. **Partial index for active customers (if status is rarely active):**
   ```sql
   CREATE INDEX idx_customers_active_id ON customers(id) WHERE status = 'active';
   ```
   Speeds the hash join by fetching only active rows immediately.

> **Caution:** Indexes will slow inserts/updates on `orders` and `customers`. Test in staging first.

---

## Plain‑Language Execution Plan Explanation (Expected After Indexes)

- The database would use `idx_orders_date_amount` to seek directly to `2023-01-01…2023-12-31`, scanning only those index entries in `amount DESC` order.
- It would then join matching `customer_id` values with the active‑customer subset from `idx_customers_active_id`.
- Because the index already provides rows in the desired order, the `ORDER BY` becomes a “free” operation — no explicit sort needed.
- The entire plan would likely switch to a Merge Join or Nested Loop with no disk spills.