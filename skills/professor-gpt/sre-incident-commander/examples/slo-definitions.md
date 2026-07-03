# Example SLO Definitions

Concrete, adaptable SLO specs. Pattern: SLI spec (what counts as good/valid, and
where it's measured) → SLO target → burn-rate alerts → agreed error budget policy.

## 1. API Availability (request-driven service)

```yaml
sli:
  name: api-availability
  # Measure at the load balancer — the service's own /health lies.
  good: http_requests_total{code!~"5..", route!="/health"}
  valid: http_requests_total{route!="/health"}
  measured_at: edge load balancer
slo:
  target: 99.9%
  window: 30d rolling          # budget = 43.2 min/month of full outage
alerts:
  - name: fast-burn            # 2% of monthly budget per hour
    expr: burn_rate_1h > 14.4 and burn_rate_5m > 14.4
    action: page               # exhausts budget in ~2 days — wake someone
  - name: slow-burn
    expr: burn_rate_6h > 6 and burn_rate_30m > 6
    action: page
  - name: trickle-burn
    expr: burn_rate_3d > 1
    action: ticket             # slow bleed — fix this week, not at 3am
```

## 2. API Latency

```yaml
sli:
  name: checkout-latency
  # Ratio SLI beats "p99 < X": it degrades gracefully and sums across windows.
  good: requests with duration < 400ms on route=/checkout/*
  valid: all requests on route=/checkout/*
  measured_at: edge load balancer
slo:
  target: 99.0%                # 1% of requests may exceed 400ms
  window: 30d rolling
notes: >
  Secondary long-tail guard: 99.9% under 2000ms. Two thresholds catch both
  "slightly slow for many" and "hanging for a few".
```

## 3. Data Pipeline Freshness

```yaml
sli:
  name: orders-mart-freshness
  # Time-based SLI: minutes in which the mart is fresh enough.
  good: minutes where (now() - max(loaded_at)) < 120m
  valid: all minutes in window
  measured_at: warehouse query on the consumer-facing table
slo:
  target: 99.5%
  window: 30d rolling          # ~3.6h of staleness allowed per month
alerts:
  - page when staleness > 120m during business hours (07:00-22:00 UTC)
  - ticket when staleness > 120m outside business hours   # no 3am pages
                                                          # for a daily report
```

## 4. Background Job Success (async work)

```yaml
sli:
  name: email-delivery
  good: jobs completing successfully within 10m of enqueue
  valid: all enqueued jobs, excluding user-cancelled
  measured_at: job queue events (enqueue → terminal state)
slo:
  target: 99.5%
  window: 28d rolling          # 28d aligns windows to weekdays
```

## Error Budget Policy (agree BEFORE the first breach)

| Budget remaining (30d) | Consequence |
|---|---|
| > 50% | Normal development; ship freely |
| 10-50% | Reliability items enter every sprint; risky launches need SRE sign-off |
| < 10% | Only reliability work and P0 fixes ship on this service |
| Exhausted | Feature freeze until the window recovers; postmortem review of spend |

## Common Mistakes to Reject

- SLI measured inside the service (misses infra, LB, and DNS failures)
- SLO copied from another team without asking what *these* users tolerate
- Alerting on raw error rate instead of burn rate (flappy AND slow-bleed-blind)
- 99.99% targets on a service with single-zone deployment — the target
  cannot exceed what the architecture can deliver
- Counting health checks, bots, or retries as valid events (inflates the denominator)
