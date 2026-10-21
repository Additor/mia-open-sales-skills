---
name: mia-forecast
description: Sorts the deals dated in a period into Commit, Best Case and Pipeline from what the buyer has said and done, and sets that beside the CRM commit so the gaps are easy to read. Not for a list of deals that drifted from the team's process (use mia-at-risk-review) or a whole-pipeline weekly page (use mia-weekly-review); try "Show my forecast", "Is the Q4 commit real?" or "Is Brightwell really Commit?"
---

# Forecast

{{SHARED}}

Before step 1, read assets/ref/shared-reports.md. Before any draft, read assets/ref/shared-writes.md.

## Purpose
Test the CRM's expectations against buyer evidence. Only buyer statements and actions are judged; the subject is CRM versus buyer and never the seller, so a gap means that the stage or close date has yet to catch up with the buyer's actual behavior, rather than any fault in a rep. It produces no probabilities and no scores, only the categories, flags, gates and signals defined in scoring-axes. It is read-only. Never change a category, close date or stage.

## Two values
CRM commit is the classification the CRM holds now: the commit or forecast-category field when one exists, otherwise the category the CRM's stage implies, mapped to the scoring-axes categories. Evidence commit is the category the buyer evidence supports. Name the source field in `crmLabel` (put it in the tile label, for example "CRM commit (Forecast category)") and in `howBuilt`. Always call the CRM value "CRM commit", never "reps say" or "<Name> says". One plain line under the header explains both values so a first-time reader needs no help.

## Pack files
- scoring-axes: `## Categories`, `## Axes`, `## Risk signals`, `## What counts as evidence`.
- deal-lifecycle: `## Pipelines and stages` (order, typical days, conditions) and `## Qualification to close`.
- market-physics: what was present in deals that closed.
- working-style: `## Recurring slips`.
- team-standards: `## Target for the period`, `## What leaders review each week`.
- crm-guide: `## Forecast fields` (which fields hold category, amount, close date, owner).

Missing or seed files follow the shared definitions: use CRM stages and classifications. Name the Economic Buyer in the pack's words.

## View and period
Apply the view rules. Title: "<Company> Forecast" for a team view, falling back to "Team Forecast"; "<user first name>'s Forecast" for a personal view, falling back to "Forecast". The period is the range the user names (one month, two months, a quarter, a date range); with none, the current quarter. Scope is open deals whose CRM close date falls in the period: what the CRM expects to close. Read separately the open deals dated within 30 days after the period; they are candidates to pull in and never enter forecast numbers. Use a target only if the user states one or team-standards holds one. Never invent a target, and never rate coverage against rules of thumb.

## Read budget
- CRM: in-scope deals by filtered query (stage, amount, close date, created date, owner, forecast category, stage-entry and close-date change history where available, next step, contacts and titles). Cap at 120 deals; when there are more, keep the 120 largest and state it, e.g. "classified the 120 largest of roughly 180 period deals".
- Notes and activities (notes, calls, emails, meetings) for every scored deal, by a few association-based batch queries, not per deal.
- Calls: summaries of all calls in the last 60 days for these deals. Full text or transcript search for at most 8 deals: the ones where the CRM and the evidence differ most, or where a summary mentions a buyer date or decision that needs exact words.
- Email: for each deal, threads with the buyer's domain over the last 60 days, read for buyer-side signals. A leader's inbox lacks rep threads: use the emails logged in the CRM and say so in `howBuilt`.
- Calendar: last 60 days and next 30 days, matched by attendee domain (held vs booked). In a leader's case, the CRM's meeting records stand in.
- Where chat and contract tools are connected: in internal deal chat, look for the name of the buyer's company, and check in the signing tool whether each contract was sent, opened or signed.

## Classification
Before classifying, read `assets/ref/mia-forecast-classification.md` and follow it for every deal: category and flags, Evidence date and `buyerDate`, the open gate (`blocker`) and `move`, the sums, and the Differences. Low categories always get a move.

## Sections, in this order
Read `assets/schemas/mia-forecast.md` before filling DATA; it holds ids, caps, field contents and word limits.
1. Header: title, the one-line explanation, tiles (deals in period, CRM commit, Evidence commit, Slip; with a target, also target and Coverage ratio) and the spread across categories.
2. Differences: where the CRM is ahead of the evidence (up to 6, team view 8), then where the evidence is ahead (up to 6), each with a category and date shift and one fact.
3. Deals: every in-period deal, up to 120, most certain first, with open gate, move, a short why, and 2 to 5 dated, sourced evidence lines. Buyer side first, with a buyer title and quote where one exists (logged summaries: `assets/ref/shared-csv-as-crm.md`); say "Economic Buyer not named on any call or email" when true; name every active signal; write "note only, unconfirmed" when a seller note is the only source.
4. Likely to slip: any deal with Slip (buyer-named date or Evidence date after the period's end), largest first. They also appear in Deals.
5. Team sweep (team view only): per rep, CRM commit and Evidence commit amounts and a Coach's question (20 words at most) naming one deal and the decision needed, for example whether a deal with no meeting booked keeps this month's close date. `children` lists that owner's deals. Largest gap first.
6. How the forecast works: the gates and signals in plain words, so anyone can check a label.

## Special cases
Read `assets/ref/mia-forecast-special-cases.md` when a source or CRM classification is missing, when the user asks about one deal (answer in chat, skip the report), and for the snapshot line at the end of the report.

## Chat reply
Layout: top items (decisions come before numbers), then key numbers. Key numbers: deals in the period and pipeline amount, Evidence commit amount, count and amount slipping past the period. Top items, each at most 15 words, leaving out empty ones, in this order: Move (every Slip deal, its Evidence date, what the buyer has not done, 8 words); Close out (the Close-out candidates among the deals read, wherever the close date falls against the period, defined in scoring-axes `## Definitions`; reason in 8 words); One buyer action (the move for the one or two deals nearest the next category, and which seller does it). A deal in both Move and Close out appears only in Close out. Team view: a Coach's question per rep after the decisions. First-run line: say "first run" and that "How the forecast works" lets anyone check a label.

Offer, in this order: a schedule for Mondays at 7:00 local, ahead of the forecast call, when a scheduling tool exists and none is set; otherwise an offer tied to a finding, such as a note for bringing the Economic Buyer to a call at one named company, or for a leader, 1:1 notes for a rep.

## Rules
- Only buyer-side evidence with a date and source moves a deal up. Seller notes, stage names and enthusiasm do not.
- Same evidence, same category: apply the gates and signals identically each run and show what was applied.
- Never invent quotes, dates or contacts. One wrong "the CFO said next quarter" on a deal signing Friday sinks the whole page.
- Never score or rank people, and never use adjectives about them: write "the CRM has it as Commit; the Economic Buyer has not joined a call".
- If the CRM and the evidence agree within a small amount, say so in one line and stop.
- Deal names are company names. Each Move carries 2 to 4 verb-first steps. Use the pack's stage names, method terms and category words.
