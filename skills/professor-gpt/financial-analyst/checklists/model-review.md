# Financial Model Review Checklist

Run before any model reaches leadership, the board, or investors. A model that fails section 1 should not proceed to section 2.

## 1. Structural Integrity
- [ ] Balance sheet balances in every period (A − L − E = 0); check row present and conditional-formatted
- [ ] Ending cash on cash flow statement ties to balance sheet cash, every period
- [ ] Net income flows correctly to retained earnings and the top of the cash flow statement
- [ ] Depreciation on the cash flow ties to the PP&E schedule
- [ ] No circular references (or intentional ones documented with iteration settings noted)
- [ ] Checks tab exists and sums to zero

## 2. Formula Hygiene
- [ ] No hardcoded numbers inside formulas (F5 → Special → scan for constants in calculation ranges)
- [ ] Formulas consistent across each row — inspect first, middle, and last period of every row
- [ ] No references to empty cells, other workbooks, or #REF/#DIV0/#N/A anywhere (COUNTIF for errors = 0)
- [ ] Named ranges or absolute references used for assumption links; no fragile long chains
- [ ] SUM ranges cover exactly the intended rows (classic bug: inserted row outside the range)

## 3. Assumption Reasonableness
- [ ] Every assumption has a source or rationale noted (prior actuals, benchmark, management target)
- [ ] Revenue growth decomposes into drivers (volume × price, or reps × productivity) — no bare CAGR applied to a total
- [ ] Growth deceleration is modeled: no company grows 100% forever; check year-over-year growth trend is plausible
- [ ] Margins converge to defensible long-term levels (compare to public comps at similar scale)
- [ ] Headcount plan implies sane revenue per employee (B2B SaaS: roughly $150k-$300k at scale)
- [ ] Terminal growth ≤ long-run GDP (2-3%); WACC and terminal growth internally consistent
- [ ] Working capital assumptions (DSO/DPO/deferred revenue) match historical actuals ±10%

## 4. Stress the Model
- [ ] Zero out revenue growth: does the model break, or degrade gracefully?
- [ ] Set the downside scenario: does cash go negative, and does the model flag it visibly?
- [ ] Move one key assumption ±20%: output moves in the right direction, proportionally
- [ ] Terminal value share of DCF < 80% of total (else extend the forecast period)
- [ ] Sensitivity tables recalculate correctly (data tables are set to automatic, not stale)

## 5. Actuals Reconciliation
- [ ] Latest actuals tie to the source system / closed books exactly (not "close enough")
- [ ] Actuals vs prior forecast variance reviewed — recurring misses in one line mean the driver logic is wrong
- [ ] Forecast switch date is current; no forecast formulas overwriting actual periods

## 6. Presentation & Handoff
- [ ] Color conventions followed (blue inputs, black formulas, green cross-tab links)
- [ ] Outputs page answers the actual question asked (runway, valuation range, hiring capacity) without spelunking
- [ ] Scenario switch works and the active scenario is labeled on every output page
- [ ] Version number bumped, change log updated, file named `model_vX.Y_YYYYMMDD`
- [ ] Sensitive tabs (comp detail) hidden or split out before external sharing

**Sign-off rule**: reviewer must be someone other than the builder, and must change at least three inputs to watch them flow through before approving.
