# Reference: Database Index Strategies & Execution Plan Nodes

## §1 Index Type Compatibility by Engine

| Index Type      | PostgreSQL | MySQL 8+ | SQL Server | Oracle   | Best For                                      |
|-----------------|------------|----------|------------|----------|-----------------------------------------------|
| B‑tree (default)| ✅         | ✅       | ✅         | ✅       | Equality, range, sorting, most common          |
| Hash            | ✅         | ❌¹      | ❌         | ❌       | Equality‑only (no range), very fast lookups   |
| GiST            | ✅         | ❌       | ❌         | ❌²      | Geometric, full‑text, custom data types       |
| GIN             | ✅         | ❌¹      | ❌         | ❌       | Full‑text search, array containment, JSONB    |
| BRIN            | ✅         | ❌       | ❌         | ❌       | Very large tables with physical order         |
| Full‑text       | GIN/GiST   | FULLTEXT | Full‑Text  | Oracle Text | Text search, LIKE '%keyword%' alternatives   |
| Clustered/Index‑Organized | ✅ (via CLUSTER) | ❌ (re‑build) | ✅ (by default PK) | ✅ (Index‑Organized Table) | Range scans on PK, physical order |

¹ MySQL supports hash indexes only for MEMORY engine; not for InnoDB. InnoDB uses B‑tree.  
² Oracle has domain indexes that can be extended for GiST‑like functionality.

## §2 Index Column Order Heuristics

- **Equality columns first** – Place columns used in `WHERE col = value` at the beginning.
- **Range / inequality next** – Columns used with `BETWEEN`, `>`, `<`, `LIKE 'prefix%'` go after equality.
- **Sort columns last** – If the query has an `ORDER BY` on a column that also appears in the WHERE, place it after the filter columns to avoid an explicit sort.
- **Covering index** – Include columns used in SELECT (if not already in index) using `INCLUDE` clause (SQL Server, PostgreSQL 11+) to allow index‑only scans.

## §3 Execution Plan Operators – Plain‑Language Key

| Operator             | Seen In                | Meaning                                                       | Performance Impact                       |
|----------------------|------------------------|---------------------------------------------------------------|------------------------------------------|
| **Seq Scan**          | All                    | Reads every row from the table.                               | Linear O(n); bad for large tables        |
| **Index Scan**        | All                    | Uses an index to find rows, then reads table (heap).          | Good for medium selectivity              |
| **Index‑Only Scan**   | PostgreSQL, Oracle     | Reads directly from the index without touching the table.     | Fastest; requires covering index         |
| **Bitmap Index Scan** | PostgreSQL, Oracle     | Combines multiple indexes into a bitmap, then fetches rows    | Useful for AND/OR conditions             |
| **Hash Join**         | All                    | Builds an in‑memory hash table from one input and probes with the other | Fast for large, unsorted inputs; needs memory |
| **Merge Join**        | All                    | Sorts both inputs and merges them. Requires both inputs sorted. | Good when indexes provide sorted data    |
| **Nested Loop**       | All                    | For each row from outer table, searches inner table.          | Can be awful if inner table large; good with small outer or indexed inner |
| **Sort**              | All                    | Explicit sorting, often spills to disk if insufficient work_mem. | O(n log n); expensive for large sets     |
| **HashAggregate**     | All                    | Groups rows using a hash table.                               | Uses memory; may spill                  |
| **Partial/Parallel**  | PostgreSQL, Oracle     | The operation is split among workers.                         | Improves speed, but may add overhead     |

## §4 Common Query Anti‑Patterns

- **Functions on indexed columns:** `WHERE YEAR(date_col) = 2024` → use `date_col BETWEEN '2024-01-01' AND '2024-12-31'`
- **Leading wildcard:** `WHERE name LIKE '%smith'` → index unusable; consider full‑text search or reverse indexes.
- **OR across columns:** `WHERE a = 1 OR b = 2` → often forces multiple index scans or Seq Scan. Tune with UNION ALL or composite index.
- **Correlated subqueries in SELECT or WHERE** → often better as JOIN or LATERAL.
- **SELECT * with DISTINCT** → DISTINCT on all columns may force large sort/hash; select only needed columns.
- **Large IN lists** – May exceed optimizer limits; consider temporary table or JOIN.
- **Implicit conversions** – `WHERE varchar_col = 123` prevents index usage, causing full scan.

## §5 Database‑Specific Optimizer Hints (Use Sparingly)

| Engine     | Hint / Command                      | Purpose                               |
|------------|-------------------------------------|---------------------------------------|
| PostgreSQL | `SET enable_seqscan = off;`         | Discourage sequential scans (session) |
| MySQL      | `FORCE INDEX (idx_name)`            | Force index usage                     |
| SQL Server | `WITH (INDEX(idx_name))`            | Force index                           |
| Oracle     | `/*+ INDEX(t idx) */`               | Optimizer hint                        |