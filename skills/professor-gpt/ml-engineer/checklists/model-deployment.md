# Model Deployment Checklist

Verify every item before promoting a model to production. Items marked
(blocker) mean: do not deploy, full stop.

## Evaluation Integrity (blocker section)

- [ ] Model beats the dumb baseline (majority/mean/last-value) by a margin larger than CV noise (mean ± std reported)
- [ ] Model beats or matches the current production champion on the SAME test set
- [ ] Test set touched exactly once, after all tuning was frozen
- [ ] Split strategy matches reality: time-based for temporal data, group-based for repeated entities (no user in both train and test)
- [ ] Leakage audit done: no scaler/encoder fit on full data, no target-derived features, no duplicates across splits, no post-event features
- [ ] Per-segment metrics reviewed (top 5 business segments); no segment regresses > 5% vs. champion
- [ ] Probabilities calibrated (reliability curve checked) if any consumer thresholds on them

## Reproducibility

- [ ] Training run logged in experiment tracker: params, metrics, git SHA, environment
- [ ] Exact training data snapshot versioned and referenced (DVC/lakeFS/table snapshot ID)
- [ ] Model artifact in the registry with lineage to run + data version
- [ ] Retraining from scratch reproduces test metric within ±1% relative
- [ ] Random seeds pinned; dependency versions locked (requirements/lockfile stored with the run)

## Serving Correctness

- [ ] Training and serving use the SAME feature transformation code (shared library or feature store) — verified, not assumed
- [ ] Golden-set parity test: 100+ examples scored offline vs. through the serving path, predictions match within tolerance (blocker)
- [ ] Input validation at the endpoint: schema, ranges, null handling; malformed input returns a clear error, never a silent default prediction
- [ ] Latency verified under load: p99 within SLO at 2x expected peak QPS
- [ ] Fallback behavior defined for model-service outage (rules, cached prediction, or safe default) and tested

## Rollout Plan

- [ ] Shadow mode completed: >= 1 week or >= 10k predictions logged and compared to champion, no anomalies
- [ ] Canary plan: 5% → 25% → 100% with promotion criteria written down (business + model metrics)
- [ ] Rollback is one action (registry stage flip / traffic switch), rehearsed, < 5 minutes
- [ ] A/B or holdout in place if the model's business impact must be measured

## Monitoring (must be live BEFORE full rollout)

- [ ] Input drift monitoring per key feature (PSI alert at > 0.2)
- [ ] Prediction distribution monitoring vs. training-time distribution
- [ ] Null-rate and out-of-range alerts on incoming features
- [ ] Ground-truth pipeline joins labels when they arrive; live metric dashboard vs. offline metric
- [ ] Alert routing defined: who gets paged, and the runbook link is in the alert
- [ ] Retraining trigger documented (schedule or drift/decay threshold)
