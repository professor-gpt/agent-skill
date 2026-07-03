# Test Plan: [Feature / Release Name]

**Author**: | **Date**: | **Build/Commit**: | **Target release**:

## 1. Objective & Scope

- **What is being tested**: one paragraph — the feature/change and its user-facing impact.
- **In scope**: components, endpoints, user roles, platforms.
- **Out of scope**: explicitly list what is NOT tested and why (owned elsewhere, unchanged, deferred).

## 2. Risk Assessment (drives everything below)

| # | Risk | Likelihood (H/M/L) | Impact (H/M/L) | Test depth |
|---|------|--------------------|----------------|------------|
| 1 | e.g., Payment double-charge on retry | M | H | Exhaustive: idempotency, concurrency, chaos on gateway timeout |
| 2 | e.g., Layout break on mobile Safari | M | L | Smoke on one device |

Rule: H/H risks get boundary + negative + concurrency cases. L/L risks get one happy-path check.

## 3. Test Approach by Layer

| Layer | What we add/verify | Owner | Est. effort |
|-------|--------------------|-------|-------------|
| Unit | New logic branches, validation rules | Dev | |
| Integration | Service + DB behavior, contract with X | Dev/QA | |
| API | Status codes, schema, authz matrix, idempotency | QA | |
| E2E | Journeys touched: [list, max 2–3 new] | QA | |
| Manual/Exploratory | 60–90 min charter: [riskiest area] | QA | |
| Non-functional | Perf baseline ±10%, a11y pass on new UI | QA | |

## 4. Test Cases (key scenarios — full set in test management tool)

| ID | Scenario | Technique | Priority | Expected result |
|----|----------|-----------|----------|-----------------|
| TC-01 | [Happy path with concrete values] | — | P1 | |
| TC-02 | [Boundary: min-1, min, max, max+1] | BVA | P1 | |
| TC-03 | [Invalid class: wrong type/format] | Equivalence | P2 | 400 + actionable error |
| TC-04 | [Invalid state transition] | State transition | P2 | Rejected, state unchanged |
| TC-05 | [Concurrent duplicate submission] | — | P1 | Exactly-once effect |

## 5. Environments & Data

- **Environments**: [staging URL, config deltas from prod, feature flags state]
- **Test data**: how created, how isolated, how cleaned up. No shared mutable accounts.
- **Access needed**: roles/tokens required and who provisions them.

## 6. Entry / Exit Criteria

- **Entry**: feature merged to RC branch; unit+integration green; environment deployed and smoke-passing.
- **Exit (release-ready)**: 100% P1 cases pass; no open S1/S2 bugs; P2 pass rate >= 95% with failures triaged; regression suite green; residual risks documented and accepted by [name].

## 7. Schedule & Responsibilities

| Activity | Owner | Start | End |
|----------|-------|-------|-----|
| Test case review with dev/PM | | | |
| Execution round 1 | | | |
| Bug-fix verification round | | | |
| Sign-off | | | |

## 8. Risks to the Plan Itself

- e.g., environment instability, late-arriving scope, single-person dependency — with mitigation for each.
