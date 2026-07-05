# Template: SQL Optimization Report

Fill this template for every optimization request.

---

## Original Query
```sql
{{PASTE_ORIGINAL_QUERY_HERE}}
```

## Performance Bottlenecks
1. **{{BOTTLENECK_1}}** – {{EXPLANATION}}
2. **{{BOTTLENECK_2}}** – {{EXPLANATION}}
…

## Optimized Query
```sql
{{OLD_OR_NEW_QUERY}}
```

> **Semantic check:** (Describe any result‑set changes, or state “Identical results guaranteed”.)

## Index Recommendations

| # | Index Name | CREATE Statement | Columns & Order | Engine‑Specific Notes |
|---|------------|------------------|-----------------|------------------------|
| 1 | `idx_…`    | `CREATE INDEX …` | (col1, col2)    |                       |
| 2 | …          |                  |                 |                       |

> **Trade‑offs:** (e.g., increased write latency, storage, maintenance)

## Execution Plan Explanation (Plain Language)

1. **Node 1:** {{EXPLAIN_IN_SIMPLE_TERMS}}
2. **Node 2:** {{EXPLAIN_IN_SIMPLE_TERMS}}
…

## Validation & Caveats
- [ ] Database engine: {{ENGINE}}
- [ ] Existing indexes considered: {{LIST}}
- [ ] Assumptions: {{IF_ANY}}