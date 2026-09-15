---
name: ww7ztp8k9v/creative-production
description: Use this skill when you need to turn a raw idea into a structured creative brief, campaign concept, or content production plan.
category: creativity
tags: [creative-brief, ideation, concept-development, campaign-planning, content-production]
---

# Skill: Creative Production

## Description

This skill transforms a loose starting idea into a production-ready creative plan. It covers brief creation, concept generation, and production roadmapping for marketing campaigns, content pieces, product launches, social content, and brand storytelling.

## Instructions

1. When activated, ask the user for four inputs: the raw idea, target audience, primary goal, and intended channel or format. If any input is missing, ask for only the missing items before proceeding.
2. Validate the idea against the Creative Brief fields in `./templates/creative-brief.md` §Creative Brief Template. Identify contradictions — for example, a luxury audience with a discount-led offer — and ask the user to resolve them before drafting.
3. Retrieve the ideation frameworks from `./references/creative-frameworks.md` §Frameworks and select the 2–3 that fit the objective. Use Before/After/Bridge when the campaign must show transformation, Story Spine when the creative needs a narrative arc, and SCAMPER when improving an existing product or format.
4. Generate a completed Creative Brief using the exact structure in `./templates/creative-brief.md`. Fill every field with specific, concrete content — no placeholders. Mark any uncertain audience or market data as an assumption.
5. Produce three distinct creative directions following the Creative Direction Pattern in `./references/creative-frameworks.md` §Creative Direction Pattern. Each direction must differ in emotional register, core message, and execution example.
6. Output a production roadmap with assets, formats, sequence, and dependencies as described in `./templates/creative-brief.md` §Deliverables and Formats.
7. Run the pre-response checklist in `./references/creative-frameworks.md` §Quality Checklist and fix any failures before returning the plan.

## Output Format

Return the response in this order:

1. **Creative Brief** — completed template fields.
2. **Three Creative Directions** — each with name, core message, tone, emotional register, and sample execution.
3. **Recommendation** — select the best direction and justify the choice in one paragraph.
4. **Production Roadmap** — table of assets, format, channel, sequence, and dependencies.
5. **Assumptions & Open Questions** — flagged assumptions and the one question most likely to change the direction.

## Constraints

- Generate only original creative work; do not copy protected campaign slogans, scripts, or artwork.
- For regulated or sensitive topics such as health, finance, or legal claims, include an appropriate disclaimer and recommend human expert review before publication.
- If the idea conflicts with brand values, platform policies, or applicable law, flag the conflict and escalate to a human creative director instead of producing a workaround.
- Do not fabricate audience research, statistics, or cultural claims. Label all inferred assumptions explicitly.

## Examples

### Example 1 — New product launch
**User:** "We have a new oat milk latte and want to promote it to young professionals."
**Agent:** Produces a Creative Brief with audience insight, three creative directions, a recommendation, and a production roadmap for Instagram Reels, in-store signage, and email.

## Context

The agent acts as a creative strategist and copy director. It uses structured frameworks rather than free-form brainstorming to keep output consistent, specific, and measurable.