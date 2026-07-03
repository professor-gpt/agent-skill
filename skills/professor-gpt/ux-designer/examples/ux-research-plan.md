# Example UX Research Plan — Onboarding Drop-off Investigation

A worked example. Adapt structure; keep the discipline of one primary question per study.

---

## Background

Analytics show 62% of new signups never connect a data source (the activation milestone). Drop-off concentrates on the "Connect integration" step (41% abandon there). We don't know *why* — analytics tell us where users leave, not what they were trying to do.

## Research Questions (prioritized)

1. **Primary**: What blocks or discourages new users from connecting a data source in their first session?
2. Secondary: Do users understand the value of connecting before being asked to do so?
3. Secondary: Which integration category do first-time users look for first, and is it findable?

Explicitly out of scope: pricing perception, feature requests from power users.

## Methods (triangulated)

| Method | Answers RQ | N | Effort |
|--------|-----------|---|--------|
| Session recordings review (existing tool) | RQ1 — where friction shows | 30 sessions | 1 day |
| Moderated usability tests on live onboarding | RQ1, RQ2 — the why | 6 (3 technical, 3 non-technical) | 4 days |
| First-click test on integration gallery | RQ3 — findability | 40 unmoderated | 2 days |

Rationale: recordings scale and are free but can't explain intent; moderated tests explain intent but n is small; first-click test gives statistical confidence on the one narrow findability question.

## Participants

- Recruited from signups in the last 14 days who did NOT activate (email invite, $50 incentive)
- Screener: decision-maker or hands-on implementer for analytics at their company; excludes competitors and UX professionals
- Mix: 3 from companies <50 employees, 3 from 50-500

## Timeline

| Week | Activity |
|------|----------|
| 1 | Screener out, recordings review, test script drafted + piloted internally |
| 2 | 6 moderated sessions (2/day, never more than 3 — moderator fatigue degrades data) |
| 2 | First-click test launched in parallel |
| 3 | Synthesis (affinity mapping), report, findings readout |

## Success Criteria for the Study Itself

- Every RQ answered with evidence, or explicitly marked "insufficient data — needs follow-up"
- Top 5 friction points ranked by (frequency × severity), each with a video clip
- At least 3 actionable design recommendations sized S/M/L with the team

## Deliverables

1. 1-page executive summary (problem, top findings, recommendations)
2. Findings deck with clips, delivered in a 30-min readout
3. Prioritized issue list in the backlog, tagged `research:onboarding-q3`

## Risks & Mitigations

- **Non-activated users hard to recruit** → over-invite 4x; fallback to activated-but-slow users
- **Live product changes mid-study** → freeze onboarding deploys during week 2 (agreed with eng lead)
- **Stakeholders want "just fix it" answers** → readout leads with the 3 recommendations, evidence second
