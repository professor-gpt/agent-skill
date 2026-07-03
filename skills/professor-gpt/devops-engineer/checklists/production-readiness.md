# Production Readiness Checklist

Work through every section before a new service takes production traffic.
A service is NOT production-ready with any unchecked item in Reliability or Security.

## Reliability

- [ ] Liveness and readiness probes defined and tested (readiness fails during startup/dependency outage)
- [ ] Minimum 2 replicas across at least 2 availability zones
- [ ] PodDisruptionBudget set (maxUnavailable: 1 or 25%)
- [ ] Resource requests set from load-test data; memory limit = request to avoid OOM surprises
- [ ] Graceful shutdown: handles SIGTERM, drains in-flight requests, terminationGracePeriod >= p99 request time + 5s
- [ ] Retries with exponential backoff + jitter on all outbound calls; circuit breakers on critical dependencies
- [ ] Timeouts explicitly set on every network call (no infinite defaults)
- [ ] Load tested to 2x expected peak; autoscaling (HPA) verified to trigger before saturation

## Security

- [ ] Container runs as non-root; readOnlyRootFilesystem where possible
- [ ] No secrets in env-var manifests or images — sourced from vault/secret manager at runtime
- [ ] Image scanned (Trivy/Grype) with zero critical CVEs; base image updated within last 30 days
- [ ] NetworkPolicy restricts ingress/egress to known peers
- [ ] Service account scoped to least-privilege RBAC; no default service account token mounted
- [ ] TLS on all external endpoints; mTLS or network isolation for internal traffic
- [ ] Dependency audit clean (npm audit / pip-audit / govulncheck) in CI

## Observability

- [ ] Structured JSON logs to stdout with request/trace IDs; no PII logged
- [ ] RED metrics exported (Rate, Errors, Duration) per endpoint
- [ ] Distributed tracing propagated (W3C traceparent / OpenTelemetry)
- [ ] Dashboards created BEFORE launch: traffic, errors, latency (p50/p95/p99), saturation
- [ ] Alerts defined on SLO burn rate, not raw thresholds; each alert links to a runbook
- [ ] On-call rotation assigned and paging tested end-to-end

## Delivery & Rollback

- [ ] Deployed via pipeline only — no manual kubectl/console access required
- [ ] Rollback rehearsed and completes in < 5 minutes
- [ ] Database migrations are backward-compatible (expand/contract pattern) and decoupled from deploys
- [ ] Feature flags in place for risky new paths
- [ ] Canary or blue-green configured with automated rollback on error-rate regression

## Operations

- [ ] Runbook covers: restart, scale, rollback, dependency outage, data restore
- [ ] Backups automated and a restore has been ACTUALLY performed, not just configured
- [ ] Cost estimate reviewed; budgets/alerts set on the service's resources
- [ ] SLOs documented (e.g., 99.9% availability, p99 < 300ms) and agreed with stakeholders
- [ ] Capacity plan reviewed for the next 6 months of projected growth
