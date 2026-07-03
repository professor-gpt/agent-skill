# Growth Experiment Brief

**Experiment ID**: EXP-[###]
**Owner**: [Name]
**Status**: Proposed / Running / Concluded
**AARRR stage**: Acquisition / Activation / Retention / Referral / Revenue
**ICE score**: I [ ] + C [ ] + E [ ] = [ ] / 10

---

## Hypothesis

> We believe that **[change]**
> for **[audience segment]**
> will result in **[expected effect]**
> because **[insight or evidence behind the belief]**.

Bad: "We believe a new homepage will increase signups."
Good: "We believe replacing the feature-list hero with an outcome headline for paid-search visitors will lift visitor→signup by 15%, because session recordings show 60% bounce within 8 seconds without scrolling."

## Primary Metric & Guardrails

- **Primary metric**: [one metric, e.g., visitor → signup rate]
- **Current baseline**: [X%] (from [date range], n = [ ])
- **Minimum detectable effect**: [Y% relative lift — be honest; <10% MDE needs big traffic]
- **Guardrail metrics**: [metrics that must NOT degrade, e.g., activation rate, unsubscribe rate — define acceptable range]

## Design

- **Type**: A/B test / holdout / pre-post / smoke test
- **Variants**: Control = [current]; Variant B = [change] (one change per variant)
- **Audience & split**: [segment], [50/50], randomized by [user/session]
- **Sample size required**: [n per variant] (from power calc at 80% power, 95% significance)
- **Expected runtime**: [days] — always run full weeks to avoid day-of-week bias; minimum 1 week, maximum 4

## Kill Criteria (decide BEFORE launch)

- Stop early if primary metric drops >[20%] with >90% confidence
- Stop early if any guardrail breaches its range for 3 consecutive days
- If runtime hits [max date] without significance: conclude "no effect," ship nothing, log learning

## Instrumentation Checklist

- [ ] Events for primary + guardrail metrics firing and QA'd in staging
- [ ] Variant assignment logged and joinable to conversion data
- [ ] Dashboard link: [url]
- [ ] Experiment does not overlap audience with: [list running experiments]

## Results (fill at conclusion)

| Metric | Control | Variant | Lift | Confidence |
|--------|---------|---------|------|------------|
| [Primary] | | | | |
| [Guardrail 1] | | | | |

**Decision**: Ship / Iterate / Kill
**Learning (one sentence, added to learnings doc)**: [What we now know that we didn't]
**Follow-up experiments spawned**: [EXP-###]
