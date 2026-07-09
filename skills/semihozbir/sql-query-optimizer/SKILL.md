---
name: semihozbir/sql-query-optimizer
description: Use this skill when you need to analyze slow SQL queries, rewrite them for better performance, recommend missing indexes, and explain execution plans in plain, non-technical language.
category: coding
tags: [sql, query-optimization, indexing, execution-plan, database, performance-tuning]
---

# Skill: SQL Query Optimizer

## Description
This skill transforms slow SQL queries into well‑performing ones by combining execution plan analysis, plain‑language explanation, targeted index suggestions, and safe query rewrites. It works across PostgreSQL, MySQL, SQL Server, and other relational databases, always prioritizing readability and safety.

## Instructions

1. **Gather context** – Ask the user for:
   - The exact slow query (with table schema if available).
   - The database system and version (e.g., PostgreSQL 16, MySQL 8.0).
   - The output of `EXPLAIN` or `EXPLAIN ANALYZE` (if present). If not provided, offer to help generate it.
   - Any known data volumes or cardinalities.

2. **Parse the query** – Extract all tables, JOINs, WHERE/HAVING predicates, GROUP BY / ORDER BY columns, subqueries, CTEs, and aggregate functions. Build a mental model of the data flow and identify the execution order.

3. **Analyze the execution plan** – If an execution plan is provided, break it down node by node:
   - Detect full table scans (`Seq Scan`, `ALL`), nested loops with large row counts, missing indexes, hash/sort operations, and high-cost nodes.
   - Correlate each slow node to the corresponding part of the query.
   - If no plan exists, infer likely problem areas from the query structure (e.g., missing indexes on filter or join columns, functions wrapped around columns, `SELECT *` on wide tables, unnecessary sorting).

4. **Explain in plain language** – Describe what the database is actually doing, step by step, and why it’s slow. Replace jargon with clear explanations:
   - “The database is reading every row from the `orders` table (a full table scan) because there’s no efficient way to find only the rows from last month.”
   - “The nested loop join is comparing every customer with every order, which becomes extremely slow as the tables grow.”
   - Avoid terms like “cardinality estimation” or “cost‑based optimizer” unless you immediately explain them.

5. **Propose concrete index improvements** – For each table, recommend indexes that directly support the query’s WHERE, JOIN, GROUP BY, and ORDER BY clauses:
   ```sql
   CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date);
   ```
   - Consider composite indexes with column order matching filter selectivity and sort needs.
   - Note any potential downsides (e.g., write overhead, space impact).
   - Explain in plain language why the index helps (“The database can jump directly to the rows for customer 42 and then pick only those from March, avoiding scanning millions of old orders.”).

6. **Rewrite the query** – Produce an optimized version that:
   - Uses sargable predicates (avoid functions on indexed columns, avoid leading wildcards in LIKE).
   - Replaces `OR` conditions with `UNION` when it allows better index usage.
   - Converts correlated subqueries to joins or derived tables when suitable.
   - Only selects the columns actually needed (avoid `SELECT *`).
   - Uses `EXISTS` instead of `COUNT(*) > 0` for existence checks.
   - Moves filtering into CTEs or derived tables to reduce intermediate row counts.
   - Preserves the exact same result set – never change query semantics.

7. **Validate the rewrite** – Verify that:
   - The output columns and data types remain identical.
   - Edge cases (NULL handling, duplicates, ordering) are preserved.
   - The recommended indexes are compatible with the database system (e.g., MySQL InnoDB vs. PostgreSQL partial indexes).

8. **Deliver the final output** in a structured, easy‑to‑read format:
   - **Plain‑Language Explanation** of the current query’s behavior and bottlenecks.
   - **Index Suggestions** with exact DDL statements and a short “why it helps” note.
   - **Optimized Query** (the rewritten SQL).
   - **Summary of Changes** – a bullet list of what was changed and the expected impact.
   Always end with a reminder to test the rewritten query and indexes on a staging environment before deploying.

## Constraints

- **Read‑only advice only** – Do not execute or modify any database objects without explicit user confirmation.
- **No destructive actions** – Never suggest dropping tables, columns, or existing indexes unless clearly flagged as high‑risk and only with user consent.
- **Explain simply** – Assume the user may not be a DBA; use everyday language when describing execution plan operations.
- **Database‑specific nuances** – Adapt syntax and index features to the stated database system (e.g., use `EXPLAIN (FORMAT JSON)` for PostgreSQL, `SHOW INDEX` for MySQL). If the system is unknown, ask.
- **Data sensitivity** – Never expose actual data values in explanations; work only with table/column names and structural information.
- **Testing mandate** – Always remind the user that performance improvements depend on data distribution and hardware, and that generated suggestions must be tested.

## Output Format

Use the following template for every response:

```
## Plain‑Language Explanation
(What the database is doing right now and why it’s slow)

## Index Suggestions
```sql
CREATE INDEX … ;
```
(Short note on how each index helps)

## Optimized Query
```sql
( Rewritten SQL )
```

## Summary of Changes
- Change 1 and why.
- Change 2 and why.

## Next Steps
- Test on staging with realistic data volumes.
- Compare execution plans before and after.
- Monitor production after deployment.
```