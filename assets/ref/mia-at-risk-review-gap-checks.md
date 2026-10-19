# At-risk review: gap checks

Read this before Part 1. Compare every in-scope deal with the standard chosen for the run, and keep the evidence for each gap: a date, a quote, or a count (logged summaries are written "Logged: <paraphrase>", never quoted; `assets/ref/shared-csv-as-crm.md`). A source that could not be checked never produces a gap; it produces "unconfirmed". Risk itself is only an active signal in the Risk signals table of scoring-axes.md; its `## Definitions` govern the period, the new-deal exemption, two-way touches, valid next steps, the Economic Buyer, Our overdue commitment, Close-out candidates and gaps versus risk. A gap never makes a deal red.

## Unkept promise
Find every promise the seller made, in a call ("I'll send the security document Friday") or an email ("pricing tomorrow"), through call action items, call summaries and sent mail; a CRM next step alone is never a promise. If the promised item has not reached the buyer by the promised date (2 working days after the promise when no date was given), it is missed. If every place it could have gone was not checked, mark it "unconfirmed", never missed, unless buyer evidence (a chase or complaint) shows it did not arrive. Unconfirmed promises stay out of red (Our overdue commitment, scoring-axes `## Definitions`). Count only seller promises here; buyer promises are the Missed buyer promise signal. A promise the user made on someone else's deal (an executive joining a colleague's call) is listed under that deal as "(<Name> owes this)".

## Quiet deal and its value
Show the days without a two-way touch (compare with the Deal quiet value in scoring-axes; zero buyer contact counts as quiet) and the deal's amount.

## Missing or lapsed next step
This is the No next step signal: use its definition and the valid next step rule in scoring-axes, and cite them. The only gap added here: after a two-way touch, allow 2 working days to book a meeting. A deal the buyer wrote to yesterday is not at risk yet; it is an Off-process gap to schedule.

## Single-threaded
This is the Single-threaded signal in scoring-axes, which states when it applies. Cite the signal; do not restate its conditions here.

## No Economic Buyer
The deal is at proposal stage or later and the Economic Buyer is not counted under the scoring-axes definition. A CRM contact role alone is unconfirmed, so name it as such.

## Champion unknown
No champion is recorded. Silent champion cannot be tested, so show this gap instead.

## Methodology gaps
A field or topic the method requires by this stage is missing (for example metrics or decision process under MEDDPICC, impact or critical event under SPICED). Name the specific missing item in the pack's words. When no method list can be inferred (no qualification table in deal-lifecycle, no method fields in the CRM), skip this check and name it in `howBuilt`.

## Close date out of step with activity
The close date is this month and the deal is quiet, early-stage, or has no price or paperwork out. A close date already past is an Overdue close date (a Close-out candidate, not a gap or Slip). Repeated moves of the close date are the Pushed close date signal.

## Stage ahead of the evidence
The stage asserts progress that the activity does not back up, such as Demo Done when the calendar has no demo, or Proposal when nothing was sent. A deal that has stayed too long in one stage is the Stalled stage signal, not a gap.

## Call not logged
A buyer call appears on the calendar or in the call recordings, and the deal has no note, activity or field change within 1 working day.

## Open request
A buyer or customer asked something by email or chat (price, document, cancellation, meeting time) and the seller side has not answered within 2 working days. Check the user's inbox, including shared ones. A customer's cancellation or complaint counts even when no deal is open. It is an open request (scoring-axes `## Definitions`): a gap, never our promise. List it under Promises with the status "open request"; it is not an unkept promise and stays out of that count.

## Untracked buyer conversation
A prospect or customer with no open deal had an external call in the last 30 days or has one booked in the next 14 days (win-back, expansion, informal pilot, a demo tomorrow). List each on one line after the deals.

## Classification
- Deal at risk (red): any Risk signal is active, including a passed next-step date or an unkept buyer promise. Use a strict reading, which keeps a given deal's status identical across every skill. Even a large deal that looks healthy is at risk when the buyer's reply is pending with no date attached.
- Off-process (gold, listed as "Needs attention"): gaps exist (methodology, no Economic Buyer, Champion unknown, open request, close date or stage mismatch, CRM not updated) but no risk signal is active.
- Close-out candidate (scoring-axes `## Definitions`): listed under Close-out candidates, up to 5, largest first. A candidate that is also red keeps its red row, tagged "Overdue close date" where the close date has passed; one that is not red is listed there only, not as Off-process.
- On track (green): nothing found.
Order red deals by amount, then nearest close date. These are states, not scores: "at risk because pricing promised on June 12 has not gone out" is actionable, "62 out of 100" is not.

## Headline numbers
Amount at risk (sum of red deals), amount gone quiet (sum of deals past the quiet threshold; say that it overlaps with at risk; a close-out candidate that is not at risk is in neither), and unkept promises this month, shown as "N (M unconfirmed)". Leave out any number that cannot be computed, for example amounts when the CRM has none.

## Gap count for the team sweep
For each deal, count its distinct reasons (active risk signals plus gaps; two signals that fire from one fact count once, per scoring-axes `## Definitions`); sum the counts per rep. Show counts only, with no rank numbers and no scores.
