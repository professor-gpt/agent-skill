# Growth Loop Examples — Worked Archetypes

Use these as blueprints. For each loop, define: the steps, the reinvestment mechanism, cycle time, and the leverage metric that compounds it.

---

## 1. Content / SEO Loop (user-generated pages)

**Archetypes**: G2, Zillow, Figma Community, Stack Overflow

```
User signs up → creates content (review, file, answer)
  → content gets indexed by Google
  → content ranks for long-tail queries
  → searchers land on content → some sign up → create more content ↺
```

- **Cycle time**: 4-12 weeks (indexing + ranking lag) — slow to start, near-zero marginal CAC at scale
- **Leverage metric**: indexed pages × avg. organic visits per page × visitor→signup rate
- **Leak points**: thin/duplicate content gets deindexed; logged-out pages must be crawlable and fast
- **Viability test**: do ≥10% of users create public, query-matching content within 30 days? If not, seed content editorially first

## 2. Viral / Referral Loop (invite-driven)

**Archetypes**: Dropbox (storage bonus), Calendly (every booking exposes the product), WhatsApp

```
User activates → product use exposes/incentivizes invites
  → invitees receive → some accept → activate → invite ↺
```

- **Math**: k-factor = invites per user × accept rate × activation rate.
  k = 0.5 means every 100 users bring 50 more (amplifier).
  k > 1 means self-sustaining growth (rare; usually requires the product to be the invite, like Calendly)
- **Cycle time matters as much as k**: k=0.4 with a 2-day cycle beats k=0.6 with a 30-day cycle over a quarter
- **Leak points**: incentivizing invites before activation attracts low-quality users; measure invitee retention separately

## 3. Paid Reinvestment Loop

**Archetypes**: DTC e-commerce, most PLG SaaS at scale

```
Spend on ads → acquire customers → collect revenue
  → reinvest gross profit into more spend ↺
```

- **Viability gate**: CAC payback < 12 months AND LTV:CAC ≥ 3. Otherwise the loop consumes cash faster than it returns it
- **Compounding lever**: creative testing velocity. Winning ad fatigue half-life is ~4-8 weeks; teams testing 10+ creatives/month sustain the loop, teams testing 2 don't
- **Leak points**: rising CPMs, audience saturation (watch frequency >3), attribution overcounting — verify with holdout geo tests quarterly

## 4. Sales-Led Loop (B2B, ACV > $10k)

```
Revenue → hire reps (ramped rep = 4-5x quota coverage)
  → reps generate pipeline → close revenue → hire more reps ↺
```

- **Viability gate**: rep payback < 12 months; magic number (net new ARR × 4 / prior-quarter S&M spend) > 0.75
- **Leak points**: rep ramp time (typically 4-6 months) hides loop health; measure cohorted rep productivity, not blended

---

## Choosing Your Loop

| If... | Primary loop |
|-------|-------------|
| Product produces shareable/public artifacts | Content/SEO |
| Product is used *with* other people | Viral/referral |
| Gross margin >70% and payback <12mo | Paid |
| ACV >$10k and sales cycle <90 days | Sales-led |

Most durable companies run one primary loop plus one secondary. Diagram yours: if you can't draw how output becomes input, you have a funnel with marketing spend on top — and growth stops when spend stops.
