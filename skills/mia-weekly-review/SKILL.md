---
name: mia-weekly-review
description: Builds one page covering every open deal in the sales pipeline (what moved, what is at risk and why, what to do next week, what closes this period), with a Team sweep and Coach's questions for leaders. Not for a Commit and Best Case breakdown (use mia-forecast) or an audit against the team's own process (use mia-at-risk-review); try "Open my Weekly Review" or "How does the pipeline look this week?"
---

# Weekly Review

## Shared rules

### Sources and pack files
Try every source (CRM, calls, email, calendar, chat, signing tool, docs, quotes) and name those that answered. Buyer chat is deal activity; check pending contracts' signing status. A CSV standing in for a CRM follows `assets/ref/shared-csv-as-crm.md`.

Read pack files (`config/`, format in SCHEMA.md) by `##` heading; defaults are the templates there. Team files outrank personal ones, except voice.md. A file that does not exist is "missing": use defaults and add one closing note that pack setup can create it. A file that exists but is unfilled (`status: seed`, or only template placeholders) is "seed": use defaults for what it lacks, treat its starting values as editable (a seed scoring-axes makes categories "starting values") and add the provisional line.

### View and scope
Role (rep, leader, both) comes from working-style, where the placeholder `<rep | leader | both>` counts as unset. When unset or absent: an explicit scope, what the user said about themselves in this conversation, else the user's email against CRM owners (most open deals: rep; few while others own most: leader; real share of both: both), else ask once, else rep. State the view at the top. For both, "my deals" gives own deals and "team" the team view; offer the other in a line. A leader with no deals gets the team view. Team scope: CRM team data, roles, then owners of deals touched in 90 days; else list owners.

Sales pipelines only (no onboarding, renewal, support, abandoned); with several, use the pack's or the largest. Last activity is the latest two-way touch on any channel. Before calling a deal quiet, verify outside the CRM field (unanswered mail inflates it; chat never shows), state the channel ("12 days, call"), and tag CRM-only verdicts "per CRM".

### Risk and evidence
Risk means an active signal in the Risk signals table of scoring-axes.md; never write thresholds elsewhere. Its `## Definitions` and `## What counts as evidence` fix every term used here. A contract unsigned 7 or more days is a missed next step. An overdue promise by either side is a signal; name who promised what.

Every fact carries source and date. Unsupported claims and unchecked sources read "unconfirmed" or "not seen", never "missed"; our own notes stay unconfirmed until the buyer backs them. Quote only words read, to the right speaker; a logged summary is no quote.

### Chat reply and offers
Chat reply: the provisional line first (only when a seed file was used); then the skill's items in its own layout, else key numbers and the top items it names; then the first-run line (report skills), the sources line (with any missing-file note and any check skipped because a seed file lacks what it needs, in one clause), one offer, and `Config:`. A skill's layout replaces only the order of its items; key numbers show only if it lists them. Keep it to one screen.

`Config:` plus the files used with versions is the last line. Offer priority: a skill-defined offer, single or ordered pair, first; else a schedule offer; else the most useful next skill not yet run here.

Scheduling: a scheduling tool is any tool that can create a scheduled or recurring task. When one exists and none is set for this skill, offer a schedule at its place in the priority; create it after a yes and never repeat a refusal. With an attached or pasted CSV as the data, say nothing about scheduling anywhere and make no schedule offer, a skill's own included. With other data and no scheduling tool, say once that a scheduler can repeat the run.

### Failures and style
Retry a failed call once, continue, mark partial totals. No CRM: follow `assets/ref/shared-csv-as-crm.md` (it covers the CSV request and the light fallback). A skill's read caps apply to records. No amounts: count deals.

Facts and next actions only; no encouragement, no emojis. Every flag gets a reason and an action, in the user's terms. Describe work, not people: no scores, rankings or personal adjectives; show good habits. Leader output is shareable; personal files never feed team totals.

Report skills also read assets/ref/shared-reports.md.
Skills that write or draft also read assets/ref/shared-writes.md.

Before step 1, read assets/ref/shared-reports.md. Before any draft, read assets/ref/shared-writes.md.

## Purpose
Produce the same one-page review every week: movement, risk with reasons, next week's actions, and what closes. Leaders also get a Team sweep with one Coach's question per rep. The skill is read-only. Never change a stage, close date or any CRM field; suggest, and let a person change it.

## Pack files
- deal-lifecycle: `## Pipelines and stages` (stage order, exit conditions, typical days) and `## Qualification to close` (method, what usually goes missing).
- working-style: role, and `## Recurring slips` (what to flag first).
- team-standards: `## What leaders review each week` (shape of the Team sweep) and `## Every deal gets` (checklist for each rep's deals).
- scoring-axes: `## Risk signals`, `## Definitions`.

Missing or seed files follow the shared definitions; without deal-lifecycle, use the CRM's own stages.

## View, title, period
Apply the view rules. Rep: "<Name>'s Weekly Review", own deals, no rollup, no owner names. Leader: "<Company> Weekly Review", team deals rolled up by rep. Without a name the shared title fallback applies. Both: team view, team header numbers, the user's own deals as one row under their name in the Team sweep. A team view puts rep and open-deal counts in `meta.view`, with the cadence ("weekly", "monthly" or "quarterly"). Label any company-wide figure "company-wide".

Review period: Moved forward and Closed look back 7 days from today; Closing looks forward 7 days (close dates from today through today+7). A Monday run is never empty. State both windows with dates in the header line (`meta.view`). A monthly or quarterly cadence looks back over the period so far and Closing runs to the period end; Next week still means the coming 7 days.

## Read budget
- CRM: a filtered query for open deals in scope, reading (stage entry date, next step, last-activity field as a starting point, owner, created date, close date, amount, stage), and also this period's closed deals with their loss reasons. Up to 100 open deals; if more, take the 100 with the nearest close dates and say "read 100 of about 340 open deals".
- Notes: at most 25 deals, only those that look at risk or close this period.
- Email: searches confirming the last two-way touch on deals about to be flagged, batching several deals per search. Never read every thread. A leader's inbox does not show rep threads, so use the emails and calls logged in the CRM.
- Calls: summaries covering the 30 days just past; full text limited to 3 deals at most, and only where a promise or concern is at stake.
- Calendar: the next 14 days. A meeting with someone on the buyer side makes a valid next step (scoring-axes `## Definitions`). A leader's calendar hides rep meetings, so use the CRM's next activity date, per CRM.
- Chat, if connected: search company names only for deals about to be called quiet.

## Deal flags
Risk is an active Risk signal; write the signal's name and its numbers ("quiet 18 days, email"). Other flags appear on the deal but do not count as risk:
- Overdue close date (never Slip): a Close-out candidate; propose a new date or a close-out. If the deal is also at risk it stays in At risk with this tag.
- Long in stage: the Stalled stage signal covers it. Where no typical days exist (deal-lifecycle missing or seed, no typical-days file), 30 or more days in one stage is a plain tag, never risk.
- Stage out of step: the proof for that stage is absent; name the gap in the user's method terms.
- Any item from Recurring slips that shows on this deal.

Every at-risk deal gets a concrete reason and one concrete action ("send the security document promised on the 14th", never "follow up").

## Sections, in this order
Read `assets/schemas/mia-weekly-review.md` before filling DATA; it holds ids, caps, field contents and word limits. Include every section even when empty.
1. Header numbers: open deals and amount, amount and count at risk, closing this period (count and amount), moved forward count.
2. Next week: the top 3 to 5 actions, each starting with a verb and naming who to contact, with deal, amount, owner (team view), reason and 2 to 4 steps.
3. Moved forward: good news, weighted like risk. Stage advances, wins, pilots or trials started, meetings with a decision-maker booked or held. A deal may appear here and in At risk (pilot started, no Economic Buyer yet); count it in both. If the CRM lacks stage history, rely on meetings that were booked and those held instead, noting that in `howBuilt`.
4. Closed: wins and losses this period at equal weight. Wins say what carried them over; losses give the CRM loss reason or "No reason logged".
5. Where deals sit: per stage in order, count, amount, amount at risk, and how many deals lack what the stage requires. Empty with fewer than 5 open deals in the view's scope.
6. At risk: all deals flagged, up to 40. Time urgency first (the soonest date that matters on the deal: close date, a promise or step due), then larger amount. The page shows the leading N set in the schema; the rest are grouped by owner.
7. Closing: deals with close dates inside the forward window, marked "on track" or "at risk", nothing in between.
8. Close-out candidates (scoring-axes `## Definitions`): count, total and names, each with its reason, overdue close date or a long silence. A deal that is also at risk appears here and in At risk.
9. Team sweep (team view only): one row per rep, ordered by amount at risk, largest first; the leader gets a row only when owning open deals. Each row carries a Coach's question (15 words at most) that points at one deal and one decision and is backed by evidence; no rankings, scores or adjectives about people. Opening the row (`children`) lists that owner's At risk and Moved forward deals. Spell each owner's name identically in every list.

## Thin or missing data
No close dates: skip Closing and flag once how many deals have none. No amounts: count deals and leave amount fields empty. No CRM: read an attached or pasted CSV per the shared rules; with none, after the one CSV request, build the light review (active conversations, people gone quiet, meetings booked) and skip pipeline amounts and stage rollups.

## Chat reply

Layout: key numbers (open deals and amount, number closing in the forward window, number at risk, number of Close-out candidates); the top 3 priorities (action, deal, why now), and in the team view each rep's Coach's question after them. Sources line: including what a missing source changed (for example, with no calendar, dated CRM next steps counted per CRM).

Offer, in this order: when a scheduling tool exists and no schedule is set for this skill, a run on Mondays at 7:00 local time (first Monday of the month for a monthly review); otherwise a step tied to this result: a Next move draft for the top deal, or for a leader, 1:1 notes for the rep with the largest amount at risk.

## Rules
- Trace every fact to a source. One wrong "quiet 20 days" on a deal someone spoke to yesterday ends trust in the page.
- If nothing is at risk, say so in one line and stop.
- The page should be skimmable within 30 seconds: put detail in the At risk rows only, and give each deal or stage in the other sections just one line.
- Deal names are company names. Every action item carries 2 to 4 verb-first steps. Use the user's stage names, method and team rules.
