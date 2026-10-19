---
name: mia-weekly-review
description: Builds one page covering every open deal in the sales pipeline (what moved, what is at risk and why, what to do next week, what closes this period), with a Team sweep and Coach's questions for leaders. Not for a Commit and Best Case breakdown (use mia-forecast) or an audit against the team's own process (use mia-at-risk-review); try "Open my Weekly Review" or "How does the pipeline look this week?"
---

# Weekly Review

{{SHARED}}

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
