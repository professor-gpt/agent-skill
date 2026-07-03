# Financial Model Structure Template

Standard workbook layout for an operating model or valuation. One concept per tab, left-to-right in dependency order — a reviewer should be able to trace any output back to a blue input cell in under a minute.

## Tab Layout (in order)

| # | Tab | Contents | Rules |
|---|-----|----------|-------|
| 1 | Cover | Model name, version, author, date, change log | Version as v1.2 (major.minor); log every structural change |
| 2 | Assumptions | ALL inputs: growth rates, pricing, headcount plan, margins, WACC | Only tab where humans type numbers |
| 3 | Revenue Build | Driver-based revenue by stream/segment | Formulas reference Assumptions only |
| 4 | Opex Build | Headcount-driven comp + vendor/program spend by department | Comp = heads × fully-loaded cost (salary × 1.25-1.4) |
| 5 | P&L | Monthly for years 1-2, quarterly/annual after | Pulls exclusively from builds |
| 6 | Balance Sheet | Working capital schedules, PP&E, debt | Balance check row: A − L − E = 0, red if not |
| 7 | Cash Flow | Indirect method from net income | Ending cash ties to BS cash |
| 8 | Scenarios | Base/upside/downside switch (single cell), scenario deltas | Switch drives Assumptions via CHOOSE/INDEX |
| 9 | Outputs | KPI dashboard, charts, sensitivity tables | No calculations, only presentation |
| 10 | Checks | All integrity checks in one place | Sum of checks = 0 means model is clean |

## Formatting Conventions (non-negotiable)

- **Blue font** = hardcoded input; **black** = formula; **green** = link from another tab; **red** = external file link (avoid entirely if possible)
- One formula per row, copied across all periods — no mid-row formula changes
- No hardcoded numbers inside formulas: `=D5*(1+Assumptions!$C$12)` never `=D5*1.15`
- Sign convention: costs negative throughout, or positive with subtraction rows — pick one, state it on Cover
- Units in headers ($k vs $m), period labels as dates not text, actuals vs forecast split marked with a bold column border

## Timeline Rules

- Monthly granularity for the first 24 months, quarterly to year 3, annual thereafter
- Actuals and forecast in the same rows; a single "last actuals" date cell drives IF-based switching
- Never mix calendar and fiscal periods without a mapping row

## Key Schedules to Include

1. **Headcount**: by department, start month per hire, fully loaded cost, drives >70% of opex in most software models
2. **ARR waterfall**: opening + new + expansion − contraction − churn = closing, monthly
3. **Working capital**: AR via DSO (start at 45-60 for B2B), AP via DPO, deferred revenue from billing terms
4. **Debt/equity**: draws, repayments, interest on average balance

## Scenario Switch Pattern

```
Assumptions!B2: scenario selector (1=Base, 2=Upside, 3=Downside)
Each scenario-driven input row:
  | Driver          | Base | Upside | Downside | Live value            |
  | New ARR growth  | 40%  | 55%    | 25%      | =INDEX(C5:E5, $B$2)   |
All model formulas reference the Live value column only.
```

## Handoff Checklist

- [ ] Checks tab sums to zero
- [ ] F5 → Special → Constants on calc tabs returns nothing unexpected
- [ ] Model recalculates in <5 seconds; no volatile functions (OFFSET, INDIRECT) in bulk
- [ ] A colleague can change one assumption and see it flow to outputs without instructions
