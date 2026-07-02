# Example: Decision Memo — CRM Solution Selection

## Input
**User prompt:**  
“We need to pick between building our own CRM or going with a SaaS. The engineering team wants to build, sales prefers something ready‑to‑use. I need a decision memo by Wednesday for the investment committee.”

**No documents attached.**

---

## Generated Decision Memo

### Decision Memo: CRM Solution Strategy

**To:** [Executive / Investment Committee]  
**From:** [Executive Name] (drafted by assistant)  
**Date:** [ASSUMPTION: Tuesday delivery to meet Wednesday committee]  
**Status:** [INTERNAL CONFIDENTIAL]  
**Decision Required:** Choose the CRM approach for the next 24 months.

---

### 1. Decision Question
Should Acme Corp **build a custom CRM** internally or **adopt a SaaS CRM platform** (e.g., Salesforce, HubSpot), considering total cost of ownership, time‑to‑market, and long‑term scalability?

### 2. Options & Analysis

| Criteria | Option A: Build In‑House | Option B: SaaS (Salesforce‑like) |
|----------|---------------------------|----------------------------------|
| **Description** | Develop a custom CRM using internal engineering team; estimated 12‑month build, full control of roadmap. | Adopt a mature SaaS platform with configuration, not custom code; go‑live in 3‑4 months. |
| **Strategic Alignment** | High if proprietary data model is a competitive differentiator. [MISSING: is the data model truly unique?] | Moderate — standardised but proven, reduces engineering backlog for other strategic projects. |
| **Financial** | Initial cost: ~$600k in engineering time; ongoing $150k/year maintenance. [ASSUMPTION: based on Tech Lead’s rough estimates — no formal quote.] | Year‑1 total cost: ~$250k (licenses + implementation partner); ongoing $180k/year. |
| **Time‑to‑Value** | 12+ months before usable; no sales‑enabling features in the interim. | 3‑4 months to initial release; sales team can pilot in Q1. |
| **Risks** | HIGH — scope creep, key‑person dependency, opportunity cost of engineers not working on core product. | MEDIUM — vendor lock‑in, data privacy concerns, configuration may never perfectly match workflows. |
| **Scalability** | Can be tailored to exact needs, but requires continuous investment. | SaaS vendors offer scalable infrastructure; feature updates are included. |

### 3. Recommendation
**Adopt a SaaS CRM platform (Option B) for the next 24 months**, with a plan to re‑evaluate after achieving full adoption and collecting workflow data.

**Rationale:**
- Time‑to‑value is critical — sales enablement is needed for the upcoming enterprise push, and a 12‑month pause is unacceptable.
- The financial comparison over 3 years is roughly parity (Build: $1.05M vs SaaS: $790k), but the SaaS option avoids opportunity cost and delivers value faster.
- The engineering team’s capacity is better spent on the core product differentiators; a custom CRM would divert scarce resources.
- **Critical assumption:** the required workflows can be modelled within a leading SaaS CRM without excessive custom coding. *If that proves false, the build option may regain viability.*

**Caveat:** This analysis relies on high‑level estimates; a formal vendor evaluation and build‑cost estimate are recommended before final commitment.

⚠️ **REQUIRES HUMAN APPROVAL** — the investment committee must approve the strategic direction and budget.

### 4. Implementation Outline (Draft)
- **Next 30 days:** Issue an RFQ to at least two SaaS vendors; engage a short‑term implementation partner.
- **Owner for evaluation:** [TO BE ASSIGNED]  
- **Target decision deadline:** 6 weeks to allow budget allocation for Q1.
- **Approval gate:** Final vendor contract requires CFO and legal review.

### 5. Approval Required
- **Investment Committee** (strategic direction)
- **CFO** (budget sign‑off)
- **Legal** (vendor terms)

*This document is decision support; final decisions rest with the committee. [INTERNAL CONFIDENTIAL]*