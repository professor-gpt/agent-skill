# Accessibility Audit Checklist (WCAG 2.2 AA)

Run axe-core first, then work through this manually — automation catches only ~40% of issues.
Mark each item PASS / FAIL / N-A. Any FAIL in sections 1-3 is release-blocking.

## 1. Keyboard (Blocking)

- [ ] Every interactive element is reachable with Tab / Shift+Tab in a logical order
- [ ] Every action operable with Enter/Space (buttons) and arrow keys (menus, tabs, radios)
- [ ] Focus indicator visible on every focusable element, ≥3:1 contrast vs adjacent colors, not clipped by overflow
- [ ] No keyboard traps; modals trap focus intentionally and Escape closes them
- [ ] Focus returns to the trigger element when a dialog/menu closes
- [ ] Skip link present and functional on multi-section pages
- [ ] Nothing important is hover-only (tooltips must be focusable/dismissible — 1.4.13)

## 2. Semantics & Structure (Blocking)

- [ ] Native elements used: `<button>` not `<div onClick>`, `<a href>` for navigation
- [ ] Exactly one `<h1>`; heading levels don't skip; landmarks (`main`, `nav`, `header`) present
- [ ] ARIA only where no native element exists; roles match behavior (a `role="tab"` implements tab keyboard semantics)
- [ ] Icon-only buttons have `aria-label`; decorative images have `alt=""`; informative images have meaningful `alt`
- [ ] Dynamic updates announced: toasts/async results via `aria-live="polite"`, errors via `role="alert"`
- [ ] Page `<title>` and `lang` attribute correct; SPA route changes move focus or announce

## 3. Forms (Blocking)

- [ ] Every input has a programmatic `<label>` (placeholder is not a label)
- [ ] Errors: identified in text, linked via `aria-describedby`, `aria-invalid` set, focus moved to first error on submit
- [ ] Required fields marked programmatically (`required`/`aria-required`), not by color alone
- [ ] Autocomplete attributes on identity fields (`name`, `email`, `tel`) — 1.3.5
- [ ] No redundant re-entry of information within a flow (3.3.7)
- [ ] Accessible authentication: no cognitive test without alternative; paste not blocked in password fields (3.3.8)

## 4. Visual (Major)

- [ ] Text contrast ≥4.5:1; large text (≥24px / 19px bold) and UI components ≥3:1
- [ ] Information never conveyed by color alone (add icon, text, or pattern)
- [ ] Layout usable at 200% zoom and 320px width without horizontal scroll (reflow)
- [ ] Text spacing overrides (1.4.12) don't break layout
- [ ] Pointer targets ≥24×24 CSS px or sufficiently spaced (2.5.8)
- [ ] Content respects `prefers-reduced-motion`; nothing flashes >3 times/second

## 5. Screen Reader Spot-Check (Major)

Do one pass with VoiceOver (Safari) or NVDA (Firefox/Chrome):

- [ ] Critical flow (sign-up, checkout, primary CTA) completable end to end
- [ ] Reading order matches visual order
- [ ] State changes are announced (expanded/collapsed, selected, loading, error)
- [ ] Tables announce headers; lists announce item counts

## Reporting

For each FAIL, record: WCAG criterion number, element/selector, user impact
(who is blocked and how), and the concrete fix. Severity: Blocker (cannot
complete a task) > Major (significant friction) > Minor (annoyance).
