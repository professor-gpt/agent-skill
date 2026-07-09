---
name: semihozbir/analytics-dashboard-advisor
description: Use this skill when you need to design or recommend analytics dashboards, including metrics, dimensions, chart choices, drilldowns, alerts, and executive summary narratives.
category: business
tags: [analytics, dashboards, data-visualization, business-intelligence, metrics]
---

# Skill: Analytics Dashboard Advisor

## Description
This skill transforms user requirements into a structured analytics dashboard blueprint. It guides the agent to interview the user about goals, audience, and data sources, then defines a coherent set of metrics, dimensions, chart recommendations, drilldown paths, alert conditions, and a template for executive summary narratives. The output is a ready-to-implement dashboard specification.

## Instructions

### 1. Activation & Context Gathering
When a user asks to design, review, or improve an analytics dashboard, immediately activate. Begin by asking targeted questions (3–5) to understand the context. Do not proceed until you have answers to at least:

- **Business objective**: What decision or action should this dashboard drive? (e.g., “increase monthly recurring revenue”, “reduce churn”, “optimize inventory”)
- **Primary audience**: Who will use the dashboard? (Executives, product managers, operations, sales team, etc.) and how often (daily, weekly, monthly).
- **Data availability**: What are the key data sources? (CRM, product DB, finance system, Google Analytics, etc.) and any known limitations (latency, missing fields).
- **Scope**: What time frame, segments, or regions should the dashboard cover?

Ask all questions in a single round where possible. Adapt follow-ups based on answers, but always keep the conversation moving toward a deliverable.

### 2. Define Core Metrics & Dimensions
Based on the gathered context, generate a tailored list of **5–10 metrics** and **3–5 dimension categories**. Use the embedded taxonomy in §4 Reference Tables of this skill, but customize to the user’s objective.

- **Metrics** must be: specific, measurable, and directly linked to the business objective. Include calculation formulas where applicable.
- **Dimensions** must include at minimum: time (day/week/month granularity), source/channel, and any business-specific categorical splits (e.g., product line, region, customer segment).
- Map each metric to its natural aggregation (SUM, AVG, COUNT, MAX, etc.) and state whether it’s a cumulative or snapshot metric.

### 3. Recommend Chart Types & Layouts
For each metric-dimension combination, select the most effective chart type. Use the chart selection heuristic (§4) and justify choices in 1-2 sentences. Always recommend:

- **Primary visual**: The main chart that answers the core question (e.g., trend line, bar chart, heatmap).
- **Supporting visuals**: 1–2 secondary charts that provide context (e.g., distribution, composition, ranking).
- **Overall layout**: A suggested grid arrangement (e.g., KPI tiles at top, trend line left, breakdown right, table below) tailored to the audience’s scanning pattern.

### 4. Define Drilldown & Interactivity Paths
Propose a drilldown hierarchy (2–3 levels deep) that allows the audience to explore from summary to detail. Specify:

- **Clickable elements**: Which chart elements trigger a drilldown (e.g., bar → list of transactions, trend point → daily breakdown by region).
- **Transition behavior**: What dimension or filter is applied at each level (e.g., click on a region → drill to country → city, keeping time range fixed).
- **Default drilldown** for the top-level metric.

### 5. Design Alerts & Thresholds
Create **3–5 alert rules** that monitor the most critical metrics. For each alert, define:

- **Trigger condition**: A clear numeric threshold with a time window (e.g., “weekly revenue drops >10% compared to same week previous quarter”).
- **Severity**: Critical, Warning, or Info.
- **Recommended notification**: Who should receive it (role or distribution list) and via which channel (email, Slack, dashboard annotation).
- **Suggested remediation**: A brief, actionable next step to investigate or respond (not a full runbook, but a pointer).

### 6. Construct Executive Summary Narrative Template
Generate a fill-in-the-blanks narrative template that can be generated from the dashboard data weekly/monthly. The template must include:

- A **headline** summarizing the overall performance against the main KPI.
- **3–4 bullet points** covering notable changes (what went up/down, by how much, and likely cause if inferable from the data).
- **Risks & opportunities** section (1-2 items each) calling out the most significant alert triggers and positive trends.
- **Call to action** sentence recommending the next meeting or decision.

Provide the template in Markdown, with placeholders for actual numbers (e.g., `{current_revenue}`, `{pct_change}`, `{top_gainer_segment}`). This template can be consumed by a reporting pipeline or a separate AI narrative generator.

### 7. Assemble & Deliver the Dashboard Blueprint
Combine all elements into a single structured Markdown output with these sections (in order):

1. **Dashboard Purpose & Audience** (one-paragraph summary)
2. **Metric & Dimension Catalog** (table: Metric | Definition | Formula | Aggregation | Supported Dimensions)
3. **Visual Design Plan** (table: Chart | Metric(s) | Chart Type | Rationale | Suggested Position)
4. **Drilldown Specification** (numbered list with source chart → drill level 1 → level 2 → notes)
5. **Alert Configuration** (table: Alert Name | Metric | Condition | Severity | Notification | Remediation Hint)
6. **Executive Summary Template** (Markdown template)

Conclude with an “Implementation Notes” bullet list covering data refresh frequency, authentication, tool-agnostic assumptions, and any caveats.

### 8. Validate & Refine
Before presenting the blueprint, perform these internal checks:
- Every metric is directly tied to the stated business objective.
- Chart types match the data and audience cognitive load (no pie charts for >5 categories, no line charts for sparse data, etc.).
- Drilldowns do not exceed 3 levels (too deep becomes analysis paralysis).
- Alert thresholds are actionable and not too noisy (avoid alert fatigue).
- The executive summary template is free of jargon and can be understood by a non-technical stakeholder.

If the user requests changes, iterate on specific sections without reprinting the entire blueprint unless asked.

## Constraints
- **Advisory only**: The output is a design blueprint, not an implemented dashboard. Do not generate code or SQL unless explicitly asked.
- **No access to live data**: All metric definitions and thresholds are based on the user’s described context; do not assume actual data values.
- **Data privacy**: Never ask for or store sensitive personal data beyond what the user voluntarily provides for dashboard design.
- **Domain boundaries**: For regulated domains (healthcare, finance, legal), add a note that compliance with respective regulations (HIPAA, SOX, GDPR) must be validated by a domain expert.
- **Tool agnostic**: The blueprint must be implementable in Tableau, Power BI, Looker, Metabase, or custom dashboards. Avoid tool-specific features unless the user specifies a platform.
- **Escalation**: If a metric formula cannot be defined without access to raw data schema, advise the user to consult their data engineer or provide sample data structure. If the business objective is too vague, ask clarifying questions before proceeding.

## Reference Tables (embedded taxonomy)

### a) Common Metrics by Domain
- **Sales / Revenue**:
  - Total Revenue (SUM)
  - Monthly Recurring Revenue (MRR)
  - Average Revenue Per User (ARPU)
  - Customer Lifetime Value (LTV)
  - Sales Cycle Length (AVG days from lead to close)
  - Win Rate (COUNT won / COUNT opportunities)
- **SaaS / Subscription**:
  - Churn Rate (COUNT lost / total customers over period)
  - Net Revenue Retention (NRR = (revenue_start + expansion - contraction - churn)/revenue_start)
  - Active Users (DAU, WAU, MAU)
  - Feature Adoption Rate (users_touched_feature / total_active)
  - Time-to-Value (days from signup to first key action)
- **Marketing**:
  - Cost Per Lead (CPL)
  - Conversion Rate (leads → opportunity → customer)
  - Return on Ad Spend (ROAS)
  - Website Session-to-Lead Rate
  - Branded Search Volume
- **Support**:
  - Average First Reply Time (minutes/hours)
  - Customer Satisfaction Score (CSAT)
  - Net Promoter Score (NPS)
  - Ticket Volume by Channel
  - Resolution Rate (resolved / total)

### b) Chart Selection Heuristic
| Data Relationship & Task               | Recommended Chart Type           | Avoid                              |
|----------------------------------------|----------------------------------|------------------------------------|
| Trend over time (single metric)        | Line chart                       | Pie, radar                         |
| Trend over time (multiple categories)  | Multi-line or small multiples    | Stacked bar with too many segments |
| Composition / part-to-whole (≤5 parts) | Stacked bar or donut             | Pie with >5 slices                 |
| Ranking (top N)                        | Horizontal bar chart             | Radial bar, packed bubble          |
| Distribution                           | Histogram or box plot            | Line chart                         |
| Relationship / correlation             | Scatter or bubble chart          | Stacked bar                        |
| Geospatial (heat map)                  | Filled map / choropleth          | Pie on map                         |
| Progress toward a target               | Gauge or bullet graph            | Pie chart                          |
| Comparison across two dimensions       | Heatmap or grouped bar           | Line chart with too many lines     |

### c) Alert Condition Patterns
- **Percent change vs prior period**: e.g., `(current_week - prior_year_week) / prior_year_week < -0.1`
- **Threshold breach**: e.g., `churn_rate > 5%`
- **Anomaly detection**: significant deviation from rolling 4-week moving average (trigger at >2 standard deviations)
- **Deadline proximity**: e.g., `days_until_quarter_end <= 7 AND revenue_to_target < 0.8`
- **Volume spike**: e.g., `support_ticket_count > avg(4w) * 1.5`

### d) Executive Summary Template

```markdown
## {Period} Executive Summary for {Dashboard Name}

**Headline:** {headline_summary}
- Overall {primary_kpi} for {period} was {current_value}, a {pct_change}% change vs. {prior_period_description}.
- The main driver of {positive/negative} change was {key_factor}, contributing {impact_value} to the total.

### Key Highlights
- **{Category 1}**: {trend_or_anomaly}. {actionable_insight}.
- **{Category 2}**: {trend_or_anomaly}. {actionable_insight}.
- **{Category 3}**: {trend_or_anomaly}. {actionable_insight}.

### Risks & Opportunities
- **Risk**: {alert_name} triggered on {date}. Investigate {area} as it may indicate {concern}.
- **Opportunity**: The {positive_metric} growth in {segment} suggests we should {recommended_action}.

### Recommended Next Steps
{call_to_action} – review the full dashboard for details.
```