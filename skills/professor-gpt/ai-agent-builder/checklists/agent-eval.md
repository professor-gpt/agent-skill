# Agent Evaluation & Ship-Readiness Checklist

Run before first deploy AND before any change to prompts, tools, models,
or retrieval. Items marked (blocker) gate the release.

## Eval Set Quality

- [ ] >= 20 eval cases at launch (target 50–200 as the agent matures), drawn from real tasks — not just synthetic happy paths (blocker)
- [ ] Case mix includes: happy paths, ambiguous requests, missing-information cases, adversarial/injection inputs, and out-of-scope requests the agent must refuse
- [ ] Every production incident/surprise added as a regression case within a week
- [ ] Expected outcomes are checkable: exact match, programmatic assertion, or a written rubric per case — no "looks good" grading

## Grading Rigor

- [ ] Primary metric = end-to-end task success rate, defined precisely (blocker)
- [ ] Trajectory metrics tracked: tool-call validity rate, redundant/looping calls, iterations per task
- [ ] LLM-as-judge (if used) validated against >= 30 human-labeled cases with > 90% agreement; judge prompt version-controlled
- [ ] Runs repeated (>= 3 seeds/samples) so pass rates carry error bars; changes compared against noise, not single runs

## Regression Gate (every change)

- [ ] Full eval suite run on the exact candidate configuration (prompt + tools + model + retrieval versions pinned together)
- [ ] Primary metric within noise band or better vs. current production config (blocker)
- [ ] Zero regressions on the designated critical-case subset (blocker)
- [ ] Cost per task and p95 latency recorded and within budget; any > 20% increase explicitly approved
- [ ] Diff of prompts/tool schemas reviewed by a second person

## Safety & Guardrails

- [ ] Prompt-injection suite passes: instructions embedded in retrieved docs / tool outputs / user uploads do not alter agent behavior (blocker)
- [ ] Destructive or irreversible tools require confirmation or human approval; verified by test, not by prompt text alone
- [ ] Tool credentials are least-privilege; agent cannot reach data outside its scope even if it tries
- [ ] Output validation live: schema checks, PII scan, and refusal behavior for out-of-scope requests verified
- [ ] Runaway guards tested: max iterations, token/cost caps, and timeouts actually trigger and fail gracefully

## Observability & Rollout

- [ ] Full trajectory tracing in production (prompts, tool calls, tokens, cost per run) with trace IDs
- [ ] Dashboards: task success proxy, tool error rate, cost/task, latency percentiles
- [ ] Escalation path implemented: agent hands off to a human with context when stuck or low-confidence
- [ ] Canary rollout plan (internal users → 5% → 100%) with rollback = config/version flip
- [ ] Feedback capture wired (thumbs/flag + trace link) and feeding the eval set
