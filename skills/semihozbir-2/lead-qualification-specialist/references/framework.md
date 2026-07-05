# Lead Qualification Framework: ICP, BANT, MEDDIC & Scoring

## ICP Criteria
Ideal Customer Profile (ICP) describes the firm that gains the most value from the product and yields the highest lifetime value. Score each criterion on a 1–5 scale.

| Criterion | 1 – Very Poor | 2 – Below Avg | 3 – Average | 4 – Good | 5 – Excellent |
|-----------|---------------|---------------|-------------|----------|---------------|
| **Industry** | Non‑target vertical (e.g., government for a startup tool) | Adjacent but low adoption | Target vertical with moderate penetration | Core target vertical, active buyer | Core target, named account list |
| **Company Size (employees)** | <10 or >10,000 (extreme) | 10–50 (very small) | 50–200 (small‑mid) | 200–1,000 (mid‑market) | 1,000–5,000 (upper mid‑market) |
| **Annual Revenue** | <$1M | $1M–$10M | $10M–$50M | $50M–$250M | $250M+ (if relevant) |
| **Geography** | Outside supported region | Partially covered | In region but remote | Primary region, city | HQ in key metro area, local presence |
| **Technology Maturity** | No stack visible | Legacy, on‑prem only | Hybrid cloud | Cloud‑native, modern toolchain | Uses complementary tools, API‑ready |
| **Funding / Growth Stage** | Bootstrapped, no growth | Early seed, uncertain | Series A, scaling | Series B‑C, well‑funded | Public or late‑stage, aggressive expansion |

**ICP Scoring example** – assign a score per row, then average (or weight if certain criteria are more important).  
- Weighted ICP score = (Industry ×0.3 + Size ×0.25 + Revenue ×0.2 + Geography ×0.1 + Tech ×0.15) / 1.0.

## BANT / MEDDIC Dimensions
Use this combined model to assess qualification depth.

| Dimension | Key Questions | Positive Signals (score 4‑5) | Negative Signals (score 1‑2) |
|-----------|---------------|------------------------------|------------------------------|
| **Pain** | What problem are they trying to solve? How acute is it? | “We lose $Xk/month,” “CEO mandate to fix,” “manual work causing delays,” “competitor gap” | “Just exploring,” no clear pain, “everything is fine” |
| **Urgency** | Why now? What is the trigger? | Contract renewal in 60 days, regulatory deadline, funding contingent on solution, executive initiated project | “No timeline,” “maybe next year,” “we’re not in a rush” |
| **Authority** | Who holds budget and decision power? | Confirmed VP/Director, part of a buying committee, has signed similar deals, already received budget approval | “I’m just doing research,” unknown decision process, no access to economic buyer |
| **Need / Solution Fit** | Does the prospect explicitly need a solution in this category? | Asked for a demo, filled out a detailed form, mentioned specific requirements | “Not sure what we need,” category mismatch |
| **Budget** | Do they have the money? | Mentioned a range (“$30K‑$50K”), Series B+, purchase order process known, vendor review underway | “No budget right now,” “too expensive,” “will figure it out later” |
| **Timing** | When will they make a decision? | <1 month, actively evaluating, finalist stage, decision date set | >6 months, “just researching,” no evaluation started |
| **Next‑Step Readiness** | Will they engage further? | Accepted calendar invite, agreed to trial, asked for pricing, provided business case | “Send me info,” refused meeting, unresponsive |

## Scoring Rubric
Assign a score 1‑5 for each dimension:

1 – No evidence, contradictory signals, or explicitly negative  
2 – Weak, unconfirmed hints  
3 – Some positive signals but missing concrete proof  
4 – Strong evidence, directly stated or verified  
5 – Exceptional fit, multiple verifiable proofs (e.g., budget confirmed by CFO, RFP in hand)

**Weighted Overall Score**

| Dimension | Weight |
|-----------|--------|
| ICP Fit   | 30%    |
| Pain      | 20%    |
| Urgency   | 15%    |
| Authority | 15%    |
| Budget    | 10%    |
| Timing    | 10%    |

`Weighted Score = Σ (Score × Weight) / Σ Weights`  
Scale to a 0‑100 percentage: `(Weighted Score / 5) × 100`

**Classification**

- Hot   → >80%  
- Warm  → 60% – 80%  
- Cold  → <60%

If Authority is ≤2 and Budget is ≤2, automatically cap the overall classification at Warm unless the user explicitly overrides (executive sponsorship pending).

## Signal Cheat Sheet
### Pain Signals (use to justify Pain score)
- “Losing deals because of slow response time”
- “Team spends 10 hours/week on manual data entry”
- “Compliance fines if not addressed by Q3”
- “Churn rate up 15% due to poor onboarding”

### Urgency Signals
- “Need a solution before our board meeting in 4 weeks”
- “Our current vendor is raising prices by 40%”
- “RFP responses due next Friday”
- “CEO asked me to fix this ASAP”

### Authority Signals
- Job title: VP, Director, Head of, Founder (if early‑stage)
- Mentioned “I have budget for this”
- Previously purchased similar tools
- Introduced by an executive sponsor

### Budget Signals
- “Budget is $50K for this initiative”
- “We just closed our Series B”
- “Finance has approved the PO”
- “We’re finalising our annual planning now”

### Negative / Disqualifying Signals
- “Just looking” – no pain, no urgency
- “I don’t have budget; maybe next quarter”
- “I’ll forward to my manager” – unknown authority
- “We use a homegrown solution” – no buying intent