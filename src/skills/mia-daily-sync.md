---
name: mia-daily-sync
description: Builds a short start-of-day page for a phone, covering today's sales meetings, replies waiting, deals at risk, and the next moves worth making. Not for one meeting in depth (use mia-meeting-prep) or one quiet deal (use mia-next-move); try "Start my Daily Sync", "What should I do today?", or "Morning rundown".
---

# Daily Sync

{{SHARED}}

Before step 1, read assets/ref/shared-reports.md.

## Purpose

Produce the page a rep or sales leader reads before the first meeting. It is read-only. Do not update the CRM, send, draft into an inbox, or create anything until the user approves.

## Pack files to read

Read these by their `##` headings. Missing or seed files follow the shared definitions; without deal-lifecycle, use the CRM's own stage names.

| File | Headings | Used for |
|---|---|---|
| working-style | Recurring slips, Standing rules, Time sinks | Slips decide what rises in Next moves; Standing rules limit every suggested action; Time sinks decide which preparation goes first in the steps |
| deal-lifecycle | Pipelines and stages, Qualification to close | Stage names, entry conditions, whether a deal is stuck, method gaps |
| buyers-and-competition | Competition | Recognising competitor names |
| scoring-axes | Risk signals, Definitions | The only source for Risks and Close-out candidates |
| team-standards | Every deal gets, What leaders review each week | Leader view only; turns on Team sweep |

## Role

The `role` in working-style wins. Without it, follow the shared rules. A person who mainly takes part in other people's deals (as contact, follower, or meeting attendee) or who has a recurring 1:1 with reps on the calendar counts as a leader and gets Team sweep.

## Read plan

Read everything before writing, inside these limits.

1. Calendar: every meeting today. Sort each into a sales call (a buyer, prospect, or customer with a CRM deal or contact, or a prospect's booking), another external meeting (vendor, partner, agency, recruiting), or internal. Note every free block of 30 minutes or more.
2. For each sales call: the matched CRM deal (stage, amount, close date, next step), its 3 to 5 latest activities, the latest call summary, and the last email or chat thread with each attendee. Check what was promised and whether it was delivered. For a new contact with thin CRM data, run one short web search for role only. Deeper research belongs to Meeting prep.
3. Since yesterday: from the start of the previous working day (Friday morning on a Monday). Buyer emails and chats received, stage changes, new deals, wins, losses, contracts signed or opened. Draw on CRM activity and any recorded stage history; with none, compare last-modified dates and mark stage changes as inferred.
4. Replies waiting: in the last 7 days, the buyer or prospect wrote last, the user has not answered, and the message holds a question, request or deadline. Other buyer-last messages go to Since yesterday. Email and direct messages only. Leave out group channels, internal threads, newsletters, system-generated mail, and answers to bulk mail, except where they pose a question to the user.
5. Pipeline: up to 150 open deals (the user's own; the team's for a leader) through filtered queries. Read notes only for deals that look risky. If there are more, say how many were read.

## Sections, in this order

Use exactly these section names and the field map in assets/schemas/mia-daily-sync.md, which you read at run time. The schema states the order rules, including the two permitted moves.

**Next moves.** The 2 to 5 most important actions. Order: overdue items first (oldest first), then upcoming ones by nearest date, ties by larger amount. An item blocking today's call is due before that call, so it leads the upcoming ones. Each begins with a verb and names the person to contact: "Send Dana the security doc before the 2pm call", never "Follow up with Acme". One line of reason and 2 to 3 steps. A clean day gets one line saying nothing is urgent and the meetings are all that is needed.

**Since yesterday.** At most 6 items, 10 words each. Mark progress, wins, and signatures as good, losses and slips as bad, and news such as a reply as neutral.

**Today's meetings.** Sales calls only, up to five lines each: time, company, type, attendees with titles, one deal line (stage, amount, close date, days since the last two-way touch), and in 25 words or fewer what happened last time and what is still open. Add one preparation action when it helps. Flag a first meeting or a person new to the deal, and attach a professional-profile link for that one time only. If the stage shows a large method gap (a pilot with no Economic Buyer), list it under what is still open. Fold vendor, partner, and internal meetings into one closing line with counts ("one agency kickoff, three internal"), and add a flag only if something must be done before them.

**Replies waiting.** At most 5: name, company, channel, what was asked, days waiting.

**Risks.** Only deals with an active signal from the Risk signals table, worst first: more active signals first, then larger amount. Count every flagged deal in the numbers, but show at most 3 per rep. Each row gives a concrete reason and one action. A deal with no recorded buyer contact gets null for quiet days. Last in Risks, one note item names the Close-out candidates (scoring-axes `## Definitions`); a deal that is also at risk keeps its risk row, tagged "Overdue close date" where its close date has passed, and one that is not at risk is not counted as a risk.

**Team sweep (leaders only).** Give each rep one line of at most 30 words, with the riskiest first: risk count, deals closing this week, and whichever single deal or decision calls for the leader's involvement (a deal due to close this week going quiet, an approval, an executive introduction, a call to join). Rep names must match the CRM owner field exactly. Opening a row shows that rep's risks as children. The full list belongs to Weekly Review. A leader's own deals appear in the sections above.

**Open time.** Start, end, and length of each block of 30 minutes or more. Do not plan the time.

## Length

Rows shown on screen must take about a minute to read, roughly 400 words or 500 when the reader is a leader. Move the rest into detail. Past a cap, group by count ("4 more team stage moves"). If the user says they are rushed and wants Markdown, keep it under 300 words with Next moves and Since yesterday complete and only today's actionable items elsewhere.

## Special cases

- No calendar: use a pasted schedule. With none, skip Today's meetings and Open time (each keeps its id with an `empty` line; the order stays fixed), add one line saying that connecting a calendar includes them, and show the Meetings today tile as "n/a" labelled "Meetings today (no calendar)". Any tile whose value is unknown reads "n/a" with the reason in its label.
- No CRM: use pasted deals or a CSV as the shared rules describe. With neither, build from email, calls, and calendar, mark stages as inferred, and say once that connecting the CRM or pasting open deals completes Risks.
- A source fails midway: retry once, continue, and note it in one line (for example, email unreadable, so Replies waiting may be incomplete).
- Calendar connected and showing no sales calls: the schema's reorder applies. A missing calendar is not this case.
- Weekend or holiday: target the following business day, and note this in the header.
- A leader with no deals of their own and no external meetings: Today's meetings keeps its id with an `empty` line. Team sweep follows Since yesterday directly.
- No history for a call: write "No history found". Never guess.

## Chat reply

Layout: the most urgent item, one line. Sources line: any source that was not connected or failed, and any missing pack file. Offer, in this order: a schedule offer when a scheduling tool exists and none is set; otherwise Meeting prep for the next sales call, Call follow-up for a call from yesterday with no follow-up yet, or Next move for a risky deal; on a clean day with nothing to offer, state that nothing needs action and end with the Config line.

## Rules

State only what was confirmed, and give promises with their dates. No cheering, no filler. Add background research only when it changes the call. Name a competitor only if it came up in a real conversation.
