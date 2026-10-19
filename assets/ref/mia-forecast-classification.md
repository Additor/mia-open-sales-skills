# Forecast: deal-level classification

Read this before classifying. It applies to every deal in scope, one deal at a time, using only what the buyer said or did. The categories, gates and signals come from scoring-axes.md (`## Categories`, `## Axes`, `## Risk signals`, `## What counts as evidence`). Nothing here creates a probability or a score.

## 1. Collect buyer evidence
For each deal, gather from batched queries (never call per deal): CRM notes and activities, calls from the last 60 days, email threads with the buyer's domain from the last 60 days, calendar events (past 60 days, next 30 days) matched by attendee domain, chat mentions by company name, and signing-tool status (sent, opened, signed).

Count only what the buyer said or did. A seller note such as "likes us" or "verbal yes" is not evidence until a buyer message, a call quote or a calendar event backs it. If a note claims something that cannot be confirmed, treat it as unconfirmed and say so in that deal's evidence. Last activity follows the shared rules.

## 2. Pick the category
0. A deal with an overdue close date (scoring-axes `## Definitions`) never counts in a forecast category: it gets no category, carries only the tag "Overdue close date", and is left out of every category sum, the spread and Differences. It still appears in Deals, last, and is counted in the Deals in period tile. Skip steps 1 to 3 for it.
1. Walk the Categories table and find the highest category whose gates all hold today: Commit, then Best Case, then Pipeline.
2. If any Risk signal is active, add the Deal at risk flag.
3. If the buyer-named decision date or the Evidence date (section 3) falls after the period, add the Slip flag, as defined in scoring-axes `## Categories`. The deal keeps the category its other evidence earns. 
4. Apply the gates exactly. Never raise a deal because it "feels close". The same evidence must always produce the same category.
5. Record in `evidence` which gates are met and name every active signal.

If scoring-axes is a seed, the page shows the provisional banner and calls the categories starting values.

## 3. Evidence date
The Evidence date is the later of two dates.
- The buyer's own date, never a CRM field. Move a phrase like "end of month" to the last day of that month, and resolve "by <weekday>" per scoring-axes `## Definitions` and record in `buyerDate` who said it, their title, when, and in which email or call. No buyer-given date: `buyerDate` is empty.
- The computed estimate: today plus the days for the remaining stages, never earlier than today (the floor applies to the estimate only). Remaining stages are the days left in the current stage (typical days minus days already in it, floor 0) plus the typical days of each later stage up to the signing stage (see scoring-axes `## Definitions`). Typical days come from deal-lifecycle, else the CRM's average days per stage, else 14 per stage. Paper process (not started, per the same Definitions) adds the typical paper-process days from deal-lifecycle, else 14. Economic Buyer not yet engaged adds the typical days of the current stage once. Add any delay the buyer has put on a pilot or evaluation. State in the deal's evidence which numbers were missing and which fallback was used.

An Evidence date after the period means Slip. Display: when the buyer gave a date, the date column shows the Evidence date. When the buyer gave none, the date column shows "not stated", the computed estimate goes in `detail` labelled "estimated" (for example "estimated Dec 4"), and Slip still rests on that estimate. Everywhere an Evidence date is shown (Differences, Deals, Likely to slip), the same rule applies.

## 4. Open gate and Move
For each deal write two short lines.
- Open gate (8 words at most): the single buyer-side thing that blocks the next category, for example "buyer has not stated a decision date", "Economic Buyer not on any call", "no reply since Oct 2", "contract process not started". A Commit deal always has a buyer date by gate, so where it lacks nothing, write that buyer date as the expected signing date.
- Move (up to 12 words, opening with a name): the one action available to the seller this week that could lead the buyer to close the open gate, supported by evidence (a date the buyer provided, someone the buyer named, a call already on the calendar). If the seller can do nothing, say that: "no action until the buyer replies" or "close out if no reply by Nov 4". When no real move exists, "close it out" is the move.

A low category with a clear move is good news and should read that way.

## 5. Numbers
- CRM commit total: sum of amounts of in-period deals the CRM holds as Commit, overdue-close-date deals left out. Evidence commit total: sum of amounts of deals whose Evidence category is Commit, with Slip deals left out. Best Case and Pipeline totals work the same way.
- Slip amount: sum of amounts of deals leaving the period; never added to an Evidence total.
- Only with a target (stated by the user or in team-standards `## Target for the period`): Commit gap is target minus Evidence commit; Coverage ratio is total in-period pipeline divided by target. Show the numbers and never judge whether coverage is enough.
- Deals with no amount are classified and listed, left out of every sum, marked "no amount", and counted in `howBuilt`.

## 6. Differences
Compare each deal's CRM category with its Evidence category.
- CRM ahead of the evidence: the CRM category is higher. Order by amount, largest first.
- Evidence ahead of the CRM: the Evidence category is higher. Include deals dated up to 30 days after the period only when their buyer evidence supports an earlier close, inside the period.
Each row shows the field, the two categories as "CRM category to Evidence category", the two dates, and one fact. Frame the gap as the stage or close date not yet matching what the buyer did, never as a person being wrong.

## 7. Row labels
The row label is the category: Commit, Best Case or Pipeline. Slip and Deal at risk are tags, never labels. Order the Deals list from most certain to least, ties broken by earlier Evidence date, with overdue-close-date deals (no label) last.
Move and Close-out lists (chat reply): a deal in both appears only in Close-out, and a Close-out candidate (scoring-axes `## Definitions`) appears in Close-out whatever the period.
