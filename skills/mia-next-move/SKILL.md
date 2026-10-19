---
name: mia-next-move
description: Gets a quiet or slipping deal moving with one specific, honest action and a message ready to send, either for one named deal or as a ranked scan of the pipeline. Not for a call that just ended (use mia-call-follow-up) or a full weekly view (use mia-weekly-review); try "Next move for <company>", "This deal went quiet, what do I send?", or "Which deals need a nudge?".
---

# Next move

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

Before any draft or change, read assets/ref/shared-writes.md.

## Purpose

Two modes. One deal: a company is named, and the output is a play plus a message. Pipeline scan: no company named, and the output is deals ranked by risk with messages drafted for the top 3. The skill is read-only: it drafts, and never sends or changes the CRM without approval.

## Decide what is at risk

Use the shared risk definition on open deals only (not won, lost, archived, or closed stages). For every flagged deal, name each active signal with its date or day count and the date of the last buyer reply. If the call rests on CRM fields alone, add "per CRM".

## Find the deal

**One deal.** Find the open deal at the named company that the user owns or shares. If there is one, proceed and name it in the deal line. If the company has several, take the one with the latest activity, say so, and list the others in one line. If there is none, report where you searched and request the precise name of the deal.

**Pipeline scan.** Apply the risk test to open deals and rank them by size (amount, stage, close date) and by severity: a broken commitment ranks above silence, and long silence above short silence. Reading is restricted to filtered CRM queries (never one record at a time), covering no more than 100 open deals, with at most 8 deals getting a full-context read. When the list is longer, start from the largest and say that, such as "reviewed the 100 biggest among 240 open deals". Show at most 10 deals in the table.

## Read the deal

- CRM: contacts, next step, close date, amount and stage, along with the 10 most recent activities and notes.
- Email and calendar: for each contact on the buyer side, the newest thread (noting requests, promises and anything unanswered), plus any meetings on the schedule.
- Calls: the latest summary. Read the transcript only when a detail that matters is missing: what matters to the buyer, objections, named people, timing.
- Pack files, by heading:

| File | Headings | Used for |
|---|---|---|
| voice | Writing patterns, Situation samples (nudge examples), Signature phrases, Avoid | Writing the message |
| deal-lifecycle | Pipelines and stages, Qualification to close | Move conditions, days in stage, what the method says is missing now |
| buyers-and-competition | Competition | Competitor handling |
| winning-plays | Plays, with each play's Answers signal | Matching an active signal to a play the team already runs |
| working-style | Recurring slips, Standing rules | Contact cadence, channels, prohibitions |
| crm-guide | Fields by moment, Data check thresholds | Exact field names in any CRM proposal |
| scoring-axes | Risk signals, Definitions | The risk test, valid next step, dates |

## Choose the play

One play per deal, whichever has the strongest evidence. Stacking angles makes a message long and easy to ignore. If a play in winning-plays matches an active signal through its Answers signal, prefer it. Otherwise use these general plays, named here for convenience:

| Play | Pick it when |
|---|---|
| Deliver what we owe | The user promised something and has not sent it. Send it now and say that is what it is |
| Answer the open request | The buyer raised a question, concern, or date that has no answer |
| Bring in the person they named | The buyer mentioned someone not yet in the deal ("our CFO will want to see this") |
| Share something relevant | A real page on the user's website answers a worry the buyer voiced; include the URL |
| Ask where the decision stands | Late stage and quiet: ask directly and lightly whether timing or priorities changed |
| Hold off | No good play exists. The item gives the reason and what to find out first or another route (a different contact, a call), and no draft message. An honest "not yet" beats "just checking in" |

## Write the message

Write in the user's voice: greeting, sign-off, length, and phrases from voice, and no signature the email tool adds.

- 120 words or fewer.
- Lead with the play's hook. Never start with "just checking in", nor with "circling back".
- Use the buyer's words in quotation marks only when the exact words were read in this run (email, call transcript); paraphrase everything else, logged summaries included (`assets/ref/shared-csv-as-crm.md`).
- End with one concrete request.
- The subject fits the play.
- It has to be ready to send as written. A value never seen follows the shared placeholder rule; if the strongest play depends on a missing fact, pick another play.
- Default to email. Use chat only when working-style Standing rules say so, or the user clearly talks with this buyer that way; say why.

## Output layout

**One deal** contains: the deal line (`<Deal> · <stage> · <amount> · at risk: <signal and date>`); `The play: <play>` with one sentence tying it to what the buyer said or promised; Subject, To and the message body (To shows the first name when no address is known; a Hold off item has no draft); and, when a CRM change fits (next step, a past close date) and a write tool exists, the exact change list with an offer to apply it.

**Pipeline scan** contains: a summary line (N of M open deals are at risk); a table with columns deal, stage, amount, why at risk, play; for each of the top 3, one sentence on the play, then Subject and body (a Hold off item has the reason and no draft).

Offer: for one deal, applying the change list when one is shown, else the shared priority. For a scan, the shared priority: its schedule offer is a run every Monday morning, and the follow-on is the next deal on the list or Meeting prep for an upcoming meeting.

## Special cases

- Leader: in a scan, cover the team's deals grouped by rep (risk count and amount, then the top deals). Reps send their own nudges, so give each rep one question for the next 1:1 (Coach's questions) instead of a buyer email. Draft messages only for deals the leader owns or asks for. Follow What leaders review each week in team-standards when it exists.
- No CRM: use an attached or pasted CSV per the shared rules; otherwise build the list from email and calendar, say it may be incomplete, and suggest once connecting the CRM or pasting a CSV.
- No risk found: say so in one line with the number of deals checked, and offer a nudge for any deal the user names.
- Offers: do not suggest a skill already run in this conversation.

## Rules

Trace everything. Each promise, name, quote and worry must trace to the user, a call, an email, or the CRM, since an invented nudge erodes more trust than silence. When a play requires a fact you lack, choose another play. One play and one request per message: a short nudge gets read, and a menu of options gets ignored. Respect Standing rules; if a rule blocks the best play, say so rather than breaking it. Never put buyer details into a saved pack file.
