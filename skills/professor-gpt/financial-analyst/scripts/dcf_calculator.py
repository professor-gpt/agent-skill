#!/usr/bin/env python3
"""
DCF Calculator with WACC x Terminal-Growth Sensitivity Table

Edit the ASSUMPTIONS block, then run:  python dcf_calculator.py
Educational tool only — not investment advice. Validate all outputs
against comparable-company multiples before relying on them.
"""

# ----------------------- ASSUMPTIONS (edit these) -----------------------
REVENUE_0 = 50_000_000        # Trailing twelve-month revenue ($)
REVENUE_GROWTH = [0.40, 0.32, 0.25, 0.20, 0.15]  # Yearly growth, forecast horizon
EBIT_MARGIN = [0.05, 0.10, 0.15, 0.18, 0.20]      # EBIT margin per forecast year
TAX_RATE = 0.25               # Effective tax rate
DA_PCT_REV = 0.04             # Depreciation & amortization as % of revenue
CAPEX_PCT_REV = 0.05          # CapEx as % of revenue
NWC_PCT_DELTA_REV = 0.10      # Change in net working capital as % of revenue GROWTH
WACC = 0.10                   # Discount rate
TERMINAL_GROWTH = 0.025       # Perpetuity growth (keep <= long-run GDP ~2-3%)
NET_DEBT = 5_000_000          # Debt minus cash ($); negative if net cash
SHARES_OUT = 10_000_000       # Fully diluted shares
MID_YEAR = True               # Mid-year convention (cash flows arrive evenly)
# ------------------------------------------------------------------------


def project_fcf():
    """Build unlevered free cash flow for each forecast year."""
    fcfs, revenue = [], REVENUE_0
    for growth, margin in zip(REVENUE_GROWTH, EBIT_MARGIN):
        prior_rev = revenue
        revenue *= (1 + growth)
        ebit = revenue * margin
        nopat = ebit * (1 - TAX_RATE)                    # After-tax operating profit
        da = revenue * DA_PCT_REV                        # Non-cash add-back
        capex = revenue * CAPEX_PCT_REV                  # Reinvestment
        delta_nwc = (revenue - prior_rev) * NWC_PCT_DELTA_REV  # Growth ties up cash
        fcfs.append(nopat + da - capex - delta_nwc)
    return fcfs, revenue


def dcf_value(fcfs, wacc, g):
    """Enterprise value = PV of forecast FCF + PV of Gordon-growth terminal value."""
    if wacc <= g:
        return float("nan"), float("nan")  # Perpetuity breaks when WACC <= growth
    pv = 0.0
    for t, fcf in enumerate(fcfs, start=1):
        period = t - 0.5 if MID_YEAR else t
        pv += fcf / (1 + wacc) ** period
    tv = fcfs[-1] * (1 + g) / (wacc - g)                 # Terminal value at horizon end
    tv_period = len(fcfs) - 0.5 if MID_YEAR else len(fcfs)
    pv_tv = tv / (1 + wacc) ** tv_period
    return pv + pv_tv, pv_tv


def main():
    fcfs, final_rev = project_fcf()

    print("Forecast unlevered FCF ($m):",
          ", ".join(f"Y{i+1}: {f/1e6:,.1f}" for i, f in enumerate(fcfs)))

    ev, pv_tv = dcf_value(fcfs, WACC, TERMINAL_GROWTH)
    equity = ev - NET_DEBT
    per_share = equity / SHARES_OUT
    tv_share = pv_tv / ev

    print(f"\nEnterprise value:   ${ev/1e6:,.1f}m")
    print(f"Equity value:       ${equity/1e6:,.1f}m  (net debt ${NET_DEBT/1e6:,.1f}m)")
    print(f"Value per share:    ${per_share:,.2f}")
    print(f"Terminal value is {tv_share:.0%} of EV"
          + ("  <-- WARNING: >80%, extend the forecast period" if tv_share > 0.8 else ""))
    print(f"Implied EV/Revenue (final year): {ev/final_rev:,.1f}x  <- cross-check vs comps")

    # -------- Sensitivity: per-share value across WACC x terminal growth --------
    waccs = [WACC + d for d in (-0.02, -0.01, 0, 0.01, 0.02)]
    growths = [TERMINAL_GROWTH + d for d in (-0.01, -0.005, 0, 0.005, 0.01)]

    print("\nSensitivity — value per share ($):")
    print("  WACC \\ g " + "".join(f"{g:>9.1%}" for g in growths))
    for w in waccs:
        row = ""
        for g in growths:
            ev_s, _ = dcf_value(fcfs, w, g)
            cell = (ev_s - NET_DEBT) / SHARES_OUT
            row += f"{cell:>9.2f}" if cell == cell else f"{'n/a':>9}"  # NaN check
        print(f"  {w:>7.1%}  " + row)

    print("\nNote: educational output only — sanity-check against market multiples "
          "and consult a licensed professional for investment decisions.")


if __name__ == "__main__":
    main()
