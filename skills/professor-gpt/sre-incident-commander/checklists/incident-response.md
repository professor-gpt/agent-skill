# Incident Response Checklist

Follow phase by phase. The IC coordinates and decides — the IC does not debug.

## Phase 0 — Declare (first 5 minutes)

- [ ] Is user impact real or plausible? If unsure, declare anyway — downgrading costs nothing
- [ ] Set severity (Sev1: most users blocked / data loss; Sev2: key flow or large subset degraded)
- [ ] Open the dedicated incident channel and bridge; all discussion moves there
- [ ] Assign IC by name ("I am IC" or "X, you are IC") — no implicit ownership
- [ ] Start the scribe log: timestamp every decision, action, and observation

## Phase 1 — Stabilize (minutes 5-15)

- [ ] IC assigns Ops Lead (hands on keyboard) and Comms Lead (status page + stakeholders)
- [ ] Post initial status: what's broken, who's affected, next update time
  - Sev1: status page within 15 minutes — "We are investigating elevated errors on X"
- [ ] **Mitigate before diagnosing.** Check the cheap reversals first, in order:
  1. Recent deploy? → roll back (don't debug forward)
  2. Recent config/flag change? → revert it
  3. Feature-flag the broken path off
  4. Failover to healthy zone/region/replica
  5. Shed load / enable degraded mode
- [ ] Any mitigation with risk of data loss requires explicit IC approval, logged by scribe

## Phase 2 — Coordinate (ongoing)

- [ ] Updates on cadence even if "no change" (Sev1: every 30 min; Sev2: 30-60 min)
- [ ] One workstream per hypothesis, one named owner each; IC tracks them, kills stale ones
- [ ] All prod changes announced in channel BEFORE execution (prevents compound failures)
- [ ] Escalate without shame: page subject-matter experts after 15 min of no progress
- [ ] IC checks for responder fatigue — hand off IC role after ~2 hours, with explicit
      "you are now IC" + 2-minute state handoff
- [ ] Comms Lead shields responders: execs and support get answers from the channel summary,
      never by pinging the Ops Lead

## Phase 3 — Resolve

- [ ] Confirm recovery from the user-side signal (SLO dashboard green), not just "process restarted"
- [ ] Watch for 30+ minutes before declaring resolved — regressions love victory laps
- [ ] Post final status page update with plain-language summary
- [ ] Explicitly hand back or stand down all paged responders

## Phase 4 — Within 48 Hours

- [ ] Create postmortem doc from `templates/postmortem-template.md`; scribe log is the timeline source
- [ ] Capture volatile evidence NOW: logs, dashboards screenshots, deploy IDs, flag states
- [ ] Schedule the postmortem review within 5 business days
- [ ] File the top 1-2 obvious action items immediately — don't wait for the meeting

## IC Anti-Patterns (self-check during the incident)

- IC is typing commands into prod → hand off command or the keyboard, not both
- Two people believe they are IC → stop, name one, log it
- Debugging root cause while users still hurt → return to the mitigation list
- Silent channel for 30+ minutes → post a status even if it's "still investigating"
- "Fixed it" without a user-side metric confirming → not fixed
