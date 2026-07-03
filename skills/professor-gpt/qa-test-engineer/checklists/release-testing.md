# Release Testing Checklist

Run before every production release. Items marked (S1-blocker) must pass —
no exceptions, no "we'll hotfix it".

## Pre-flight

- [ ] Scope confirmed: diff reviewed, changed areas mapped to test suites
- [ ] Risk assessment done: what is the worst plausible failure of this release?
- [ ] Test environment matches prod config (feature flags, env vars, data shape)
- [ ] Test data prepared and isolated; no dependence on leftover state
- [ ] All quarantined/skipped tests reviewed — none silently hiding a real regression in changed areas

## Automated Gates (S1-blocker)

- [ ] Unit + integration suites green on the release candidate commit (not "green yesterday")
- [ ] E2E critical journeys green: signup, login, core workflow, payment/checkout if applicable
- [ ] API contract tests pass against the RC build
- [ ] No new S1/S2 bugs open against changed components
- [ ] Static analysis / dependency audit shows no new critical findings

## Functional Verification

- [ ] Each ticket in the release verified against its acceptance criteria (not just "code merged")
- [ ] Boundary and negative cases executed for new input fields (empty, max length, invalid type, injection strings)
- [ ] Error paths verified: user sees actionable messages, not stack traces or blank screens
- [ ] Permission matrix spot-checked: lowest-privilege role cannot reach new admin features
- [ ] Backward compatibility: old clients / previous app version still work against new API

## Non-Functional

- [ ] Performance smoke: p95 latency on key endpoints within SLO, compared to previous release baseline (±10%)
- [ ] No new console errors / unhandled promise rejections on core pages
- [ ] Accessibility quick pass on new UI: keyboard navigation, labels, contrast
- [ ] Cross-browser sanity on new UI: latest Chrome, Firefox, Safari; one mobile viewport
- [ ] Data migration (if any) tested on a prod-sized snapshot AND rollback rehearsed (S1-blocker)

## Regression

- [ ] Full regression suite executed (or risk-based subset with justification documented)
- [ ] Exploratory session (60–90 min, charter-based) on the riskiest changed area
- [ ] Known fragile areas adjacent to changes manually sanity-checked

## Release Decision

- [ ] Go/no-go recorded with named approver
- [ ] Residual risks written down explicitly ("untested: X, mitigation: Y")
- [ ] Rollback plan documented and rollback trigger criteria agreed (e.g., error rate > 1% for 5 min)
- [ ] Monitoring dashboard + alerts confirmed live for changed components
- [ ] Post-release verification plan: who checks what within 30 minutes of deploy
