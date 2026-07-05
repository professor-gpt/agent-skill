---
name: semihozbir-2/sql-performance-optimizer
description: Use this skill when the user asks to analyze slow SQL queries, suggest performance improvements, rewrite queries, recommend indexes, or explain a query execution plan in plain language.
category: coding
tags: [sql, query-optimization, performance-tuning, database, execution-plans, indexing]
---

# Skill: SQL Performance Optimizer

## Description
Analyzes slow SQL queries across PostgreSQL, MySQL, SQL Server, and other major databases. Rewrites queries for optimal performance, recommends missing or suboptimal indexes, and translates execution plans into plain-language explanations. Always preserves semantic correctness unless explicitly instructed otherwise.

## Instructions

1. **Gather context:** Ask the user for the database engine (e.g., PostgreSQL, MySQL, SQL Server, Oracle, SQLite) and the exact slow query. If available, request table schemas (including existing indexes, column types, and cardinalities) and the actual execution plan output (EXPLAIN ANALYZE, EXPLAIN PLAN, etc.). If no plan is provided, state that the analysis will be based on theoretical heuristics and ask the user to confirm by running the suggested plan.

2. **Parse and analyze the query:**
   - Structure: joins types, subqueries, CTEs, UNIONs, window functions.
   - Heuristics: SELECT * (avoid unless needed), missing WHERE clauses on indexed columns, non‑sargable conditions (functions on indexed columns), implicit type conversions, inefficient JOIN orders, correlated subqueries that could be JOINs, missing LIMIT, redundant DISTINCT, OR conditions that disable index usage.
   - Check the query against the **query anti-patterns** in `references/database-index-strategies.md` §4.

3. **Interpret the execution plan (if provided):**
   - Map each plan node to the plain‑language definitions in `references/database-index-strategies.md` §3.
   - Identify high‑cost nodes (e.g., Seq Scan on large tables, sluggish nested loops, expensive sorts and hashes).
   - Explain in plain language what the database is doing, why it’s slow, and where it spends most time.

4. **Design index recommendations:**
   - Propose covering indexes, multi‑column indexes in the right order (equality columns first, range last), partial indexes where appropriate.
   - Use the index type compatibility matrix in `references/database-index-strategies.md` §1 to suggest appropriate index types (B‑tree, Hash, GiST, GIN, BRIN, etc.) for the target engine.
   - For each recommendation, provide the exact CREATE INDEX statement and the reasoning.

5. **Rewrite the query:**
   - Produce an optimized version that preserves the original semantics.
   - Apply rewrites like: converting subqueries to JOINs, moving predicates closer to table access, splitting OR into UNION ALL, using EXISTS instead of IN for large sets, pushing aggregations earlier, using CTEs or temporary tables for reuse, avoiding SELECT *.
   - If the rewrite changes result ordering (e.g., removal of ORDER BY if unnecessary), flag it.

6. **Generate the final output:**
   - Use the template in `templates/output-template.md` to produce a structured report.
   - Include: original query, identified bottlenecks, optimized query, index recommendations (with create statements), step‑by‑step execution plan explanation in plain language, and any cautions.
   - Add a “Trade‑offs” section noting potential write‑performance impact from new indexes or query complexity.

7. **Validate completeness:**
   - Ensure all suggestions are specific to the user’s database engine (refer to `references/database-index-strategies.md` for dialect‑aware syntax).
   - Confirm the recommended indexes do not duplicate existing ones (ask the user for current indexes if not provided).
   - Warn if the optimization relies on assumptions about data distribution or statistics.

## Constraints

- **No schema guesses:** If table schemas are missing, ask the user before recommending filters or joins that depend on column names.
- **Semantic equivalence:** Never change the meaning of the query unless the user explicitly requests alternative output (e.g., “can I get partial results faster?”). Flag any change in results.
- **Index overhead:** Always mention that new indexes will slow down INSERT/UPDATE/DELETE operations and consume disk space.
- **Database‑specific features:** Do not recommend features unsupported by the user’s engine. Consult `references/database-index-strategies.md` for compatibility.
- **Security:** Do not execute any SQL directly; only generate text. Never store or transmit the user’s schema data externally.
- **Escalation:** If the query involves large‑scale data warehousing or requires physical database design changes (partitioning, sharding), advise consulting a DBA.

## Output Format

Strictly follow the template in `templates/output-template.md`. The report must be self‑contained and ready for a developer to act upon.