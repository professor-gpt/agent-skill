# Postmortem: [Short incident title]

> **Blameless reminder**: We assume everyone acted reasonably given the information
> they had. We name systems and processes, not people. "Engineer X made a mistake"
> is banned; "the deploy process allowed an unvalidated config to ship" is a finding.

## Summary

| Field | Value |
|---|---|
| Incident ID / Sev | INC-____ / Sev_ |
| Date & duration | YYYY-MM-DD, HH:MM–HH:MM UTC (__ min) |
| Author(s) | |
| Status | Draft / Reviewed / Action items complete |
| User impact | e.g. "12% of checkout requests failed for 47 minutes (~8,400 users)" |
| Error budget consumed | e.g. "31 min of the 43.2 min monthly budget (72%)" |
| Detection | Alert / customer report / employee — name the specific signal |

**One-paragraph narrative**: What happened, in plain language a new hire understands.

## Timeline (UTC)

All times from the scribe log. Include detection gap and decision points, not just actions.

| Time | Event |
|---|---|
| HH:MM | Trigger event (deploy, config change, traffic shift, hardware failure) |
| HH:MM | First user impact begins ← **impact start** |
| HH:MM | Alert fired / report received ← **detection** (gap: __ min) |
| HH:MM | Incident declared Sev_, IC assigned |
| HH:MM | Mitigation attempted: ______ (worked? y/n) |
| HH:MM | Impact ends ← **mitigation** (time to mitigate: __ min) |
| HH:MM | Incident resolved / monitoring confirmed clean |

## Contributing Factors (plural — there is never exactly one)

1. **Trigger**: the proximate change or event.
2. **Latent condition(s)**: what was already fragile that made the trigger dangerous.
3. **Detection gap**: why did it take __ minutes to notice? What signal was missing?
4. **Mitigation friction**: what slowed the fix (missing rollback, unclear ownership, stale runbook)?

## What Went Well / What Was Lucky

- Went well: (fast rollback, good scribe log, clean comms...)
- Lucky: (happened during business hours, senior engineer online by chance...)
  — luck items are risks: convert each into an action item.

## Action Items

Every item MUST have an owner and a due date. Prioritize items that remove the
failure class, not just this instance. Cap at ~5 — a 20-item list means zero get done.

| # | Action | Type | Owner | Due | Ticket |
|---|--------|------|-------|-----|--------|
| 1 | | Prevent | | | |
| 2 | | Detect faster | | | |
| 3 | | Mitigate faster | | | |

Types: **Prevent** (remove failure mode) > **Detect** (shrink detection gap) >
**Mitigate** (shrink recovery time) > **Process** (comms, roles, runbooks).

## Review

- [ ] Reviewed in postmortem meeting on YYYY-MM-DD
- [ ] Shared with the wider org (link)
- [ ] Action items tracked in the team backlog with the incident tag
