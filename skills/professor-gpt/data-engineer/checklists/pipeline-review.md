# Pipeline Review Checklist

Work through every section. Mark each item PASS / FAIL / N-A and report failures by severity.

## 1. Idempotency (Critical)

- [ ] Re-running any task for the same logical date produces identical output (no duplicates, no drift)
- [ ] Writes use MERGE or DELETE+INSERT scoped to a partition — never blind append
- [ ] Tasks read the run's data interval (logical date), not `now()` / wall-clock time
- [ ] No task mutates state outside its declared output (hidden side effects, shared temp tables)
- [ ] Partial-failure recovery: a crash mid-write leaves the target either untouched or fully written (staging table + atomic swap, or transactional MERGE)

## 2. Backfills (Critical)

- [ ] Backfill uses the exact same code path as a scheduled run
- [ ] A 1-year backfill is parallelizable (no serialized dependency on previous run's output unless truly cumulative)
- [ ] Backfill cost estimated: rows × runs × warehouse cost — flag anything over ~$500 for approval
- [ ] Downstream consumers are notified/handled when historical partitions are rewritten

## 3. Data Quality (Critical)

- [ ] Primary keys tested `unique` + `not_null` on every model
- [ ] Foreign keys tested with `relationships` against dimensions
- [ ] Source freshness declared with warn/error thresholds matched to pipeline cadence
- [ ] At least one row-count reasonableness check per fact table (±30% of trailing 7-day average)
- [ ] Test failures actually block downstream models (severity `error`, not everything `warn`)

## 4. Scheduling & Orchestration (Major)

- [ ] `catchup`/backfill behavior explicitly set, not left to defaults
- [ ] Retries configured: 2-3 retries with exponential backoff for transient failures
- [ ] Timeouts set on every task (default to 2x p95 runtime)
- [ ] SLA/freshness alert exists and pages the owning team, not a shared channel nobody reads
- [ ] No sensor polling loops holding worker slots — use deferrable operators or event-driven triggers
- [ ] Dependencies declared through datasets/assets where supported, not implicit timing ("runs at 6am because upstream is usually done by 5")

## 5. Late & Bad Data (Major)

- [ ] Lookback window for late-arriving data defined (typical: 3-7 days) and documented
- [ ] Malformed records quarantined to a dead-letter table with the raw payload — never silently dropped
- [ ] Schema drift handling defined: new columns land automatically or fail loudly (choose one, deliberately)
- [ ] Timezone handling explicit: all timestamps stored UTC, event-time vs ingestion-time distinguished

## 6. Performance & Cost (Major)

- [ ] Tables > 10M rows use incremental materialization
- [ ] Partition/cluster keys match the top consumer filter columns
- [ ] No SELECT * from wide raw tables in incremental logic
- [ ] Lakehouse only: file compaction scheduled; target file size 128 MB-1 GB
- [ ] Warehouse credits/slots tagged by pipeline for cost attribution

## 7. Operability (Minor)

- [ ] Model/table descriptions state the grain in one sentence
- [ ] Runbook exists: how to rerun, how to backfill, who owns it
- [ ] Lineage is inspectable (dbt docs, Dagster asset graph, or equivalent)
- [ ] Secrets pulled from a secret manager — zero credentials in code or DAG files

## Verdict

- **Block deployment**: any Critical failure
- **Fix within one sprint**: Major failures
- **Track in backlog**: Minor failures
