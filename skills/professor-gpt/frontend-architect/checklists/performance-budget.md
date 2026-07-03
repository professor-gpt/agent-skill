# Performance Budget Checklist

Budgets are measured at p75 on real-user data (CrUX / RUM) and enforced in CI with
Lighthouse on a throttled profile (Moto G Power class, Slow 4G). A budget without
a failing CI check is a wish.

## 1. Core Web Vitals Targets (p75, mobile)

| Metric | Budget | Regression alert |
|---|---|---|
| LCP | ≤ 2.5 s | +200 ms week-over-week |
| INP | ≤ 200 ms | +50 ms week-over-week |
| CLS | ≤ 0.1 | +0.02 week-over-week |
| TTFB | ≤ 800 ms | +100 ms week-over-week |

## 2. Resource Budgets (per route, gzip/brotli)

- [ ] Initial JS ≤ 170 KB (SPA) / ≤ 100 KB (content site with RSC)
- [ ] Initial CSS ≤ 50 KB; critical CSS inlined ≤ 14 KB
- [ ] Fonts: ≤ 2 families, ≤ 4 total files, WOFF2 only, subset to used scripts
- [ ] Hero/LCP image ≤ 150 KB, AVIF/WebP with responsive `srcset`
- [ ] Total page weight ≤ 1 MB first load; third-party JS ≤ 100 KB and async
- [ ] CI fails on bundle growth >10 KB without an approved justification

## 3. LCP Diagnostics

- [ ] LCP element is server-rendered HTML, not injected by client JS
- [ ] LCP image: `fetchpriority="high"`, preloaded, and NOT `loading="lazy"`
- [ ] No render-blocking third-party scripts before LCP; `preconnect` to critical origins
- [ ] HTML streamed/cached at the edge; document TTFB under 800 ms

## 4. INP Diagnostics

- [ ] No long tasks >50 ms on the interaction path (check DevTools Performance)
- [ ] Expensive updates wrapped in `useTransition` / deferred with `useDeferredValue`
- [ ] Lists >100 rows virtualized; tables paginate or window
- [ ] Input handlers do work ≤ a few ms; heavy computation moved to Web Workers
- [ ] Hydration cost bounded: islands / RSC / `dynamic()` for below-the-fold widgets

## 5. CLS Diagnostics

- [ ] All `<img>`/`<video>` have width+height (or aspect-ratio)
- [ ] Space reserved for ads, embeds, banners, and async content (min-height skeletons)
- [ ] Fonts use `font-display: swap` with size-adjusted fallback (fontaine / size-adjust)
- [ ] No layout-shifting content injected above existing content after load
- [ ] Animations use `transform`/`opacity` only — never top/left/width/height

## 6. Dependency Gate (run before every `npm install <pkg>`)

- [ ] Checked cost on bundlephobia — is it >10 KB gzip?
- [ ] Could ≤30 lines of local code do it? (dates: prefer `Intl`; utils: write it)
- [ ] Tree-shakeable ESM? Zero-install alternatives (native dialog, CSS)?
- [ ] Maintained (commit in last 6 months) and not duplicating an existing dep?

## 7. Monitoring

- [ ] RUM collects LCP/INP/CLS with route + device dimensions
- [ ] Alerts on p75 regression thresholds above, routed to the owning team
- [ ] Lighthouse CI runs on every PR against the 3 highest-traffic routes
