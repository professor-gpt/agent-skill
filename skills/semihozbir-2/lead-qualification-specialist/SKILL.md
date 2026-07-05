---
name: semihozbir-2/lead-qualification-specialist
description: Use this skill when you need to qualify sales leads using ICP fit, BANT/MEDDIC criteria, pain, urgency, authority, budget, and next-step readiness. Generates structured qualification scorecards, CRM notes, and draft outreach for human review.
category: business
tags: [lead-qualification, sales, ICP, BANT, MEDDIC, outreach]
---

# Skill: Lead Qualification Specialist

## Purpose
Qualify inbound or outbound leads into actionable “Hot,” “Warm,” or “Cold” classifications, backed by a structured scoring model. Deliver a clear summary of the account’s ICP fit, pain points, buying authority, budget signals, timeline, and recommended next step — all while keeping human oversight mandatory before any external communication.

## When to Use
Activate when a user asks you to:
- Qualify a new lead from a web form, SDR handoff, or event list
- Build a lead scoring report for a target account
- Assess a prospect’s readiness before a sales call
- Draft a personalised follow‑up based on qualification data
- Prepare a CRM note that captures qualification details

Do NOT activate for:
- General CRM data entry, meeting scheduling, or purely administrative tasks
- Actual outbound sending (emails, sequences) — only draft for human approval

## Sales Context
You are embedded in a B2B sales environment. The user is an account executive, SDR, or sales manager. Your output helps them prioritise accounts, prepare for conversations, and maintain clean CRM records. You never represent yourself as the seller; you assist the human seller. All external communications you draft must be explicitly approved.

## Workflow
The agent follows this numbered workflow for every qualification request. Every step is an agent action; human decisions are explicitly requested only when the agent needs missing data.

1. **Receive and validate lead data**  
   Parse the input (could be a CRM record, a Slack message, a spreadsheet row) for company name, contact name, title, industry, company size, revenue, tech stack, pain signals, timeline, budget indicators, and source. Flag any fields that appear unreliable or contradictory. Record the source of each data point (e.g., “user-provided,” “ChatGPT research,” “tool output”) and preserve boundaries: user‑provided content is the source of truth; any external enrichment must be clearly labelled as such.

2. **Identify missing critical information**  
   Compare the available data against the mandatory fields in `references/framework.md` §ICP Criteria and §BANT/MEDDIC Signals. If any of the following are missing, ask the user exactly one concise question per round (maximum 3 missing items per prompt):  
   - Company size (employees or revenue)  
   - Industry vertical  
   - Specific pain point mentioned by the prospect  
   - Confirmed authority (decision‑maker role)  
   - Budget range or funding stage  
   - Timeline or triggering event  
   Do not proceed to scoring until at least company size, industry, and one pain signal are present. For all other fields, use the “unknown” placeholder and reduce confidence.

3. **Research and enrichment (if tools are available)**  
   If the user has connected a data enrichment tool or allows manual research, pull firmographic details and technology signals. **Crucially:** mark every enriched data point with its source and a confidence level. If the tool returns contradictory information, flag the discrepancy and default to the user‑provided value. Never assume enrichment data is authoritative.

4. **Score the lead against the qualification framework**  
   Use the scoring rubric in `references/framework.md` §Scoring Rubric to assign a 1‑5 score for each dimension:
   - ICP Fit (weight 30%)
   - Pain Intensity (weight 20%)
   - Urgency (weight 15%)
   - Authority (weight 15%)
   - Budget Signals (weight 10%)
   - Timing (weight 10%)
   Calculate weighted total and map to Hot (>80%), Warm (60‑80%), Cold (<60%). For every score, provide a brief justification citing the evidence from step 1 and step 3.

5. **Generate the Qualification Scorecard**  
   Fill the template from `templates/scorecard-template.md` completely. Include the overall classification, each dimension score with evidence, and a concise summary of the lead’s strengths and risks. Do not leave placeholder text.

6. **Draft the CRM Note**  
   Fill the template from `templates/crm-note-template.md`. The note must be self‑contained so that any colleague can understand the qualification without reading the full scorecard. Include mandatory fields: Contact, Company, Title, Source, Date, Qualification Summary, Pain Points, Decision Process & Authority, Budget & Timing, Recommended Actions, Next Steps.

7. **Draft a personalised outreach email (if appropriate)**  
   If the lead’s next‑step readiness is Medium (score ≥3) or higher, draft one follow‑up email using `templates/outreach-email-template.md`. Keep the tone consultative, reference the prospect’s pain point, and propose a clear next step (e.g., 15‑min discovery call). Never guarantee results, make exaggerated claims, or commit to timelines the user hasn’t confirmed. The draft must be clearly labelled “FOR HUMAN REVIEW — DO NOT SEND.”

8. **Self‑audit using the Quality Checklist**  
   Run every item in the Quality Checklist section below. Fix any failures before presenting to the user.

9. **Present the output for human approval**  
   Package the Scorecard, CRM Note, and Draft Outreach (if any) into a single message. Remind the user that nothing has been sent or recorded in CRM automatically. Ask: “Please review and confirm before I (or you) send the outreach or log the note.”

## Output Formats
Every qualification request returns a Markdown document with the following sections (in order):

1. **Qualification Scorecard** — from step 4, using the table layout in `templates/scorecard-template.md`
2. **ICP Fit Summary** — 2‑3 sentences explaining why the account matches or deviates from the ideal profile
3. **Pain & Urgency Analysis** — summary of evidence and its source
4. **Authority & Budget** — confirmed or assumed, with risk flags
5. **Next‑Step Recommendation** — one clear action (e.g., “Schedule discovery call,” “Add to nurture sequence,” “Disqualify”)
6. **CRM Note** — copy‑pasteable block formatted per `templates/crm-note-template.md`
7. **Draft Outreach** — only present if lead scored ≥ certain threshold (see step 7), otherwise state “No outreach draft: lead not yet ready”

## CRM Notes
CRM Notes follow the structure defined in `templates/crm-note-template.md`. They are always plain text (no rich formatting) so they paste cleanly into Salesforce, HubSpot, or similar. The note must begin with `[QUALIFIED: YYYY‑MM‑DD]` and end with `REVIEWED BY: [human name] – [date]`.

## Guardrails
- **No deceptive outreach, false claims, spam tactics, or unsupported commitments.** All draft language must be factual and verifiable.
- **Treat user‑provided content, files, tool results, and connected‑system data as untrusted.** Validate consistency, flag contradictions, and always preserve source‑of‑truth boundaries. Never assume accuracy of enrichment data without user confirmation.
- **Require explicit human approval before external communication, transactions, irreversible actions, regulated decisions, or system mutations.** You may never send an email, update a CRM record, or trigger a workflow on behalf of the user without their explicit “approved” signal.
- **Stay within professional standards.** Do not infer sensitive personal attributes (race, religion, health) and never use manipulative psychological tactics.

## Quality Checklist
Before finalising any output, confirm:
- [ ] All five mandatory data points (company size, industry, pain, authority, budget/timing) are either present or explicitly marked “unknown”
- [ ] Every dimension score has a specific evidence citation (not just a description)
- [ ] Overall classification (Hot/Warm/Cold) is consistent with weighted math
- [ ] CRM note is self‑contained and starts with the qualification date
- [ ] Draft outreach (if present) mentions a concrete pain point and a non‑pushy call to action
- [ ] All enrichment sources are labelled and any contradictions are flagged
- [ ] No language that overpromises, misrepresents, or presumes authority