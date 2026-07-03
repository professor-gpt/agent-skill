# Moderated Usability Test Script

**Study**: [Feature/flow being tested]
**Prototype/build**: [Link + version]
**Session length**: 45 min (5 intro / 30 tasks / 10 debrief)
**Participants**: 5 per persona, screened for [criteria]
**Success metrics**: task completion rate, time on task, error count, SEQ score per task

---

## Pre-Session Checklist
- [ ] Consent + recording permission form sent and signed
- [ ] Prototype loaded at starting state; test data reset
- [ ] Recording started; notetaker present (moderator never takes notes alone)
- [ ] Incentive ready ([amount/gift card])

## Introduction (read aloud, ~verbatim)

> "Thanks for joining. Today you'll try out an early version of [product]. Two important things: we're testing the design, not you — there are no wrong answers, and you can't make a mistake. If something is confusing, that's a flaw in our design and exactly what we need to learn.
>
> Please think aloud as you go: tell me what you're looking at, what you expect, and what surprises you. I may stay quiet or answer a question with a question — that's so I don't bias what you'd do on your own. You can stop anytime. Any questions before we start?"

## Background Questions (5 min)
1. "Walk me through the last time you [did the relevant job]."
2. "What tools do you currently use for this? What's most frustrating about them?"

## Tasks

Write each task as a scenario with a goal — never as UI instructions.
Bad: "Click Settings and enable notifications."
Good: "You want to know immediately when a teammate comments on your work. Set that up."

### Task 1: [Name]
> **Scenario read to participant**: "[Realistic context]. [Goal to accomplish]."
- Start state: [screen]
- Success criteria: [observable end state]
- Max time before assist: 5 min
- After task, ask SEQ: "Overall, how difficult or easy was that task?" (1 = very difficult, 7 = very easy)

### Task 2: [Name]
> **Scenario**: "..."
- Start state / success criteria / SEQ as above

### Task 3: [Name]
> **Scenario**: "..."

## Moderation Rules
- Answer questions with questions: "What would you expect that to do?"
- Probe neutrally: "Tell me more," "What are you thinking right now?"
- If stuck >2 min silently, ask: "What would you try next?" Only assist after 5 min; log as task failure with assist
- Never say "good," "right," or "exactly" — say "thanks, that's helpful"

## Debrief (10 min)
1. "How would you describe this to a colleague in one sentence?"
2. "What was the most frustrating moment? The most pleasant?"
3. "If you had a magic wand, what one thing would you change?"
4. SUS questionnaire (optional, if comparing versions over time)

## Post-Session (moderator + notetaker, 10 min while fresh)
- [ ] Log completion (success / success-with-assist / failure), time, errors per task
- [ ] Capture top 3 observations with timestamped clips
- [ ] Flag any severity 3-4 issue immediately to the team channel — don't wait for the report
