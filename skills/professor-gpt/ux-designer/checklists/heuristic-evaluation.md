# Heuristic Evaluation Checklist

Evaluate one flow at a time (not isolated screens). Record every finding as:
`[H# / Severity 0-4] Location — Evidence — Recommended fix`

Severity scale: 0 not a problem · 1 cosmetic · 2 minor · 3 major (fix before release) · 4 catastrophic (blocks task).

## H1 — Visibility of System Status
- [ ] Every click/tap gives feedback within 100ms (pressed state, spinner, optimistic UI)
- [ ] Operations >1s show a progress indicator; >10s show percent or steps remaining
- [ ] Current location is visible (active nav state, breadcrumbs, step indicator)
- [ ] Async results (saves, syncs, sends) confirm success explicitly

## H2 — Match Between System and Real World
- [ ] Labels use the user's vocabulary, not internal or database terms
- [ ] Information order matches the user's mental workflow, not the schema
- [ ] Icons are conventional or paired with text labels

## H3 — User Control and Freedom
- [ ] Destructive actions are undoable (prefer undo toast over confirm dialog)
- [ ] Multi-step flows allow going back without losing entered data
- [ ] Modals can be dismissed via X, Escape, and outside click
- [ ] No forced tours or unskippable interstitials

## H4 — Consistency and Standards
- [ ] Same action = same label, icon, and placement everywhere
- [ ] Platform conventions respected (back gesture, form patterns, link styling)
- [ ] Design system components used; one-off variants justified in writing

## H5 — Error Prevention
- [ ] Inputs constrained where possible (date pickers, dropdowns, input masks)
- [ ] Inline validation fires on blur, not only on submit
- [ ] Irreversible actions require explicit confirmation naming the object ("Delete 'Q3 Report'?")
- [ ] Defaults are safe and sensible

## H6 — Recognition Rather Than Recall
- [ ] No information must be remembered from a previous screen
- [ ] Recently used items, search history, and suggestions are surfaced
- [ ] Field labels remain visible after input (no placeholder-only labels)

## H7 — Flexibility and Efficiency of Use
- [ ] Keyboard shortcuts exist for frequent actions (and are discoverable)
- [ ] Bulk actions available where users operate on many items
- [ ] Smart defaults prefill from context; forms remember prior choices

## H8 — Aesthetic and Minimalist Design
- [ ] Each screen has one clear primary action
- [ ] No competing calls-to-action of equal visual weight
- [ ] Content-to-chrome ratio favors content; decorative elements earn their place

## H9 — Error Recognition, Diagnosis, and Recovery
- [ ] Error messages state what happened, why, and the next step — in plain language
- [ ] No raw error codes or stack traces shown to end users
- [ ] Errors appear adjacent to their source, and focus moves to them
- [ ] Failed submissions preserve all entered data

## H10 — Help and Documentation
- [ ] Contextual help (tooltips, inline hints) exists at points of likely confusion
- [ ] Empty states explain what belongs there and how to create it
- [ ] Help content is searchable and task-oriented ("How do I X"), not feature-oriented

## Accessibility Add-on (run every time)
- [ ] Text contrast ≥ 4.5:1 (3:1 for large text); UI component contrast ≥ 3:1
- [ ] Touch targets ≥ 44×44px with ≥ 8px spacing
- [ ] Full flow completable by keyboard alone; visible focus indicator throughout
- [ ] Images and icons carry alt text or aria-labels; form fields programmatically labeled

## Wrap-up
- [ ] All severity 3-4 findings have an owner and a ticket
- [ ] Findings deduplicated across evaluators (2-3 evaluators catch ~75% of issues)
- [ ] Top 5 findings summarized in one page for stakeholders
