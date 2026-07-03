# Tool Definition Template

Tools are the highest-leverage prompt surface in an agent. Use this template
for every tool; then score it against the quality bar at the bottom.

## Template (JSON Schema style — adapt to your framework)

```json
{
  "name": "search_orders",
  "description": "Search customer orders by status, date range, or free text. Use this when the user asks about order history, delivery status, or refunds. Do NOT use for creating or modifying orders (use update_order). Returns at most 20 orders sorted by most recent; if more exist, the response includes 'has_more': true — narrow the filters rather than paginating blindly. Example: to find last week's delayed orders for customer 4821, call with {\"customer_id\": \"4821\", \"status\": \"delayed\", \"created_after\": \"2026-06-27\"}.",
  "input_schema": {
    "type": "object",
    "properties": {
      "customer_id": {
        "type": "string",
        "description": "Internal customer ID (numeric string, e.g. '4821'). NOT the email address — resolve emails via lookup_customer first."
      },
      "status": {
        "type": "string",
        "enum": ["pending", "shipped", "delayed", "delivered", "refunded"],
        "description": "Filter by order status. Omit to include all statuses."
      },
      "created_after": {
        "type": "string",
        "description": "ISO date YYYY-MM-DD. Only return orders created on or after this date."
      },
      "query": {
        "type": "string",
        "description": "Free-text match against product names and order notes. Keep under 10 words; use keywords, not full sentences."
      }
    },
    "required": ["customer_id"]
  }
}
```

## Description checklist — every tool description must state

1. **What it does** — one plain sentence, no marketing.
2. **When to use it** — the trigger conditions in the agent's task language.
3. **When NOT to use it** — name the sibling tool to use instead (this single line prevents most tool-confusion failures).
4. **What it returns** — shape, limits (max items, truncation), and how to detect "there's more".
5. **One concrete example call** — real-looking values, not `"foo"`.

## Error responses — return guidance, not stack traces

```json
// BAD  — wastes a loop iteration, teaches the agent nothing
{ "error": "ValidationError at line 142" }

// GOOD — the agent can self-correct on the next call
{ "error": "invalid_date_format",
  "message": "created_after must be YYYY-MM-DD, got '3/4/26'. Example: '2026-03-04'." }

// GOOD — empty result is NOT an error; say what to try next
{ "results": [], "hint": "No orders matched status='delayed'. Try omitting status or widening created_after." }
```

## Quality bar (score each tool 0–2 per row; < 8 total = rewrite)

| Criterion | 0 | 2 |
|---|---|---|
| Distinctness | Overlaps another tool's purpose | An agent (or new hire) never hesitates between them |
| Granularity | One meaningful unit of work per call | Requires 3+ chained calls for one obvious task |
| Param clarity | Names like `data`, `flag`, `value` | Every param has format, example, and units |
| Error design | Raw exceptions bubble up | Every failure mode returns actionable guidance |
| Safety | Destructive with no confirm/dry-run | Idempotent, or two-step confirm for irreversible actions |

Final rule: keep the toolbox at **5–15 tools**. If you're above that, split
the agent or add a router — don't keep stuffing the belt.
