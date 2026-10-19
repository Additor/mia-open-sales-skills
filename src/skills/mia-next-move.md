---
name: mia-next-move
description: Gets a quiet or slipping deal moving with one specific, honest action and a message ready to send, either for one named deal or as a ranked scan of the pipeline. Not for a call that just ended (use mia-call-follow-up) or a full weekly view (use mia-weekly-review); try "Next move for <company>", "This deal went quiet, what do I send?", or "Which deals need a nudge?".
---

# Next move

{{SHARED}}

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
