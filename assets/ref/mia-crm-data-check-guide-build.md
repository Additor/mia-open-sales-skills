# CRM data check: building the guide

Use when the guide is built. The result is crm-guide.md, written in the order of the headings in `config/crm-guide.md`, because other skills look sections up by name.

## What to learn

Work from filtered queries and totals. Leave out pipelines the pack labels retired and those with no deal created in the past 12 months. Learn:

1. Pipelines and stages: every sales pipeline in use and its stage order.
2. How deals move: the days spent in each stage (read from stage entry dates or history; failing that, the span between creation and close, flagged as such), the portion advancing against the portion lost or gone quiet, and what typically precedes a move (more attendees at a demo, a quote going out, agreement to a pilot), as seen in activity, calls and email. Deals stall where open ones accumulate and linger longest; name that stage and the usual reason.
3. When fields fill: fill rate per field, overall and per stage. A field that is populated on nearly all deals beyond a certain stage, but seldom earlier, gets updated at that stage. A field populated on under 1 deal in 20 is in effect ignored. Record which fields get changed following a call (amount, close date, next step) and how soon.
4. The deal field list (name, type, choices) and, if the connector exposes it, the CRM's own stage-by-stage required fields.
5. Process: the pack's stage conditions and method. Where the pack deems a method field important yet it is almost never populated (e.g. a decision-process or champion field), treat it as a gap to report, not a field to disregard.
6. Leader only: anything flagged non-negotiable beneath `## Every deal gets` in team-standards turns into a required field or check. Point out where reps diverge (amount is filled at Discovery by one rep and at Pilot by others).

## Drafting

Write from what was read, not from a generic list. Begin from a baseline of lead source, one contact or more, close date and amount, plus a next step (satisfied by a valid next step per scoring-axes `## Definitions`: a booked buyer meeting or a dated task, or with no calendar a dated next-step field), then let the data adjust it. Where amount appears on almost all late-stage deals but rarely at the opening stage, make it required from the point where it becomes routine, and state that. Remove or relabel whatever is absent from actual CRM usage. Where the CRM holds no proposal artifact, infer Proof by stage from buyer-side evidence of that stage's work (price, budget, security, legal or contract talk) or a two-way touch within 30 days, and label it "(inferred from the CRM)". Include what closed-lost deals need, usually a loss reason, when the CRM has such a field. If the CRM already has required-field rules, show them as they are and add only what is missing.

## Confirmation message

One message. Lead with what the person is least likely to know about their own pipeline.
- The stage flow, roughly how many weeks deals spend in each stage, and how many move on after what.
- The stage where deals stall most and the usual reason.
- Which fields to update after a call and which at milestones.
- Fields required on every open deal, and those added per stage with what must have happened to be in that stage.
- Fields nobody uses, which will be ignored.
- At most one question, for example: "Field X is filled on 3 of 41 deals, but the pack calls it important at stage Y. Make it required from Y, or ignore it?" Skip the question if the data already answered everything.
- A closing line: say "looks right", or correct it in one line.

Use the CRM's real field names, stage names, and counts. Mark estimates. If non-sales pipelines (renewal, partner, support) exist, ask about them here and drop them from the guide if the person does not want them.

## Saving the guide

Use the template headings in order: Pipelines in scope, Fields by moment, Required fields (a table for every deal, a second for stage-added fields), Fields to ignore, Allowed values (exact choices for list fields, and topics with no field), Capture map (each item a call or email can reveal and its CRM field, or "no field"), Forecast fields, Data check thresholds (how overdue a close date must be before it is stale, what qualifies as a next step, the duplicate rule, anything the person added). Stage conditions and days in stage stay in deal-lifecycle and are not repeated here.

Keep it general and durable: field names, stage names, timing, rules. No deals, buyers, companies, or amounts beyond ranges. It says how the CRM is used, not what it contains today. Frontmatter per `config/SCHEMA.md`, `status: seed`.

Provide the saving instructions a single time, placed in the first report's own message. If a download cannot be made, give a copy block titled crm-guide.md. Outside Claude, say to save it wherever the tool keeps attachments. Note for a leader, in one line, that reps may keep a copy of this file in their own space so all treat the CRM uniformly.
