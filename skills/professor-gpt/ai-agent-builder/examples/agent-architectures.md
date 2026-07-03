# Reference Agent Architectures

Match the task to the lowest tier that works. Each pattern lists when it wins,
when it fails, and realistic cost/latency expectations.

## 1. Augmented single call (Tier 1)

```
user input → [retrieve context] → one model call (maybe structured output) → answer
```

- **Wins**: classification, extraction, drafting, Q&A over a known corpus.
- **Fails when**: the task needs external actions or multi-step lookup.
- **Cost/latency**: 1 call, sub-second to a few seconds. Exhaust this tier first — with good retrieval and a tight prompt it covers a surprising share of "agent" requests.

## 2. Fixed workflow / router (Tier 2)

```
input → classifier/router → branch A: chain [call → transform → call]
                          → branch B: different chain
```

- **Wins**: known, repeatable processes (triage → draft → verify); routing distinct request types to specialized prompts.
- **Key trick**: add a cheap verification step at the end (schema check or small-model critique) — catches most quality issues for one extra cheap call.
- **Fails when**: users go off-script; branches multiply past maintainability.
- **Cost/latency**: 2–5 calls, deterministic and easy to debug. Prefer over a free-running agent whenever the steps are knowable in advance.

## 3. Tool-using agent loop (Tier 3)

```
loop (max 10–20 iters, cost cap, loop detection):
  model → tool call → observation (truncated) → model → ... → final answer
```

- **Wins**: open-ended tasks where the path is unknown — debugging, research over live systems, multi-source questions, customer ops.
- **Design musts**: 5–15 sharp tools; errors returned as guidance; scratchpad for state that must survive context pressure; summarize history past ~60% of the window.
- **Fails when**: no measurable success criterion (agent can't tell it's done), or tools are so fine-grained the loop burns iterations on plumbing.
- **Cost/latency**: 5–20+ calls, 10s–minutes. Budget and cap explicitly.

## 4. Orchestrator + subagents (Tier 4)

```
orchestrator: plans, delegates, synthesizes
  ├─ subagent A (own context, own tools)  ← runs in parallel
  ├─ subagent B (own context, own tools)
  └─ subagent C ...
```

- **Wins**: parallelizable research (fan out queries, fan in findings); tasks whose working context would blow one window; genuinely distinct toolsets (coder + reviewer, researcher + writer).
- **Rules**: subagents return **compressed findings**, not transcripts; orchestrator never forwards raw subagent context; each subagent has its own eval.
- **Fails when**: used to mirror an org chart; agents mostly pass messages (collapse them); debugging spans 4 contexts for a 1-context problem.
- **Cost/latency**: 10–50x Tier 1. Justify with evals showing Tier 3 fails.

## 5. Cross-cutting: evaluator-optimizer loop

```
generator → output → evaluator (rubric) → pass? ship : feedback → generator (max 2–3 rounds)
```

Bolts onto any tier. Wins when quality is checkable (code compiles, citations resolve, rubric scores). Cap rounds — returns diminish sharply after round 2.

## Cost & latency levers (apply at every tier)

| Lever | Typical saving | Catch |
|---|---|---|
| Model tiering (small model for routing/summaries, large for reasoning) | 5–20x on routed calls | Route accuracy needs its own eval |
| Prompt caching (stable system prompt + tools first) | Up to ~90% on cached input tokens | Order prompt so the stable prefix never changes |
| Truncate/summarize tool outputs before re-injecting | 2–5x context reduction | Keep IDs and error details intact |
| Parallel tool calls / subagents | Wall-clock, not tokens | Only for independent operations |
| Cap max output tokens per step | Bounded worst case | Leave headroom for legitimate long answers |

**Decision rule**: write the eval set first, run it against Tier 1, and climb
one tier at a time only when the numbers say you must.
