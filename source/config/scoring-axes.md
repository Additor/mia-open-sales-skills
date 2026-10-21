---
file: scoring-axes
scope: team
version: 0.2.0
updated: YYYY-MM-DD
owner: <Head of Sales or Sales Manager>
status: seed
---

# Scoring axes

The standard that forecasts, weekly reviews, and at-risk checks apply to every deal. It works with categories and named signals. It has no numeric scores and no weights. Edit it as your process changes; each edit raises the version, and every output states the version it used.

## Categories

A deal lands in the highest category whose gates it passes. Two flags can be added on top: Deal at risk and Slip.

| Category | Gates (all must hold) |
|---|---|
| Commit | The Economic Buyer has taken part directly · the buyer has stated a decision date in their own words (a decision process, where described, goes in the evidence) · a valid next step that involves the buyer (see Definitions) · no risk signal is active |
| Best Case | The champion is engaged and answering · a valid next step that involves the buyer (see Definitions) · at least one Commit gate is still open |
| Pipeline | Any other open deal dated inside the period |

Deal at risk is set when any risk signal is active. Slip is set when the buyer-named decision date, or the Evidence date (the realistic finish date mia-forecast works out), falls after the period; the deal keeps the category its other evidence earns. A close date already in the past is not Slip: it is "Overdue close date", listed under Close-out candidates (see Definitions).

## Axes

| Axis | Evidence that counts | Where to look |
|---|---|---|
| Economic Buyer | Spoke on a call, wrote in a thread, attended, or was named as approver (see Definitions) | Calls, email, CRM contact role |
| Champion | Someone on the buyer side who replies and pushes the deal internally; engaged means recorded and Silent champion not active | Email, calls, CRM |
| Decision process | Steps and a date as the buyer describes them | Calls, email |
| Paper process | Paper process started (see Definitions) | Email, signing tool, calls |
| Next step | A valid next step (see Definitions) | Calendar, CRM |
| Threading | Number of different buyer contacts with a two-way touch recently | Email, calendar, calls |

Paper process is optional as a Commit gate. Turn it on for deal sizes where paperwork usually decides timing, and write the size here: <amount range>.

## Risk signals

This table is the one definition of Deal at risk. Every skill reads it from here and none carries its own thresholds. Starting values below are placeholders. Replace them with numbers from your own closed deals, ideally after a calibration run.

| Signal | Active when | Starting value |
|---|---|---|
| Silent champion | The champion's last reply or attendance is more than N days ago. Cannot be tested with no champion recorded (see Definitions) | N = 10 |
| Deal quiet | The last two-way touch with anyone on the buyer side is more than N days ago, or there has been none (see Definitions) | N = 14 |
| No next step | No valid next step (see Definitions) | none |
| Our overdue commitment | We promised the buyer something by a date and it has not gone out, as confirmed under Definitions | N = 2 working days late |
| Competitor mention | The buyer named a competitor within N days and has not stated a preference | N = 30 |
| Single-threaded | Just one person on the buyer side has had a two-way touch during the last N days, and the deal is past the first third of the stages (see Definitions) | N = 30 |
| Stalled stage | Days in the current stage exceed the typical days in deal-lifecycle.md by this factor | 1.5 |
| Pushed close date | The close date moved this many times inside the period (see Definitions) | 2 |
| Missed buyer promise | The buyer committed to something by a date and it passed by more than N working days. A buyer promise recorded only in our own summary stays "unconfirmed" until buyer evidence shows it missed | N = 2 |

Deals created less than 14 days ago are exempt from Silent champion, Deal quiet, Stalled stage and Single-threaded; No next step and the other signals still apply. Closed deals are never flagged. Close-out candidates (see Definitions) are listed for clean-up and are not a risk by themselves.

## Definitions

The one place these terms are defined; other files point here.

- Within N days: N days back inclusive, so an event N+1 days ago is outside.
- Period: in mia-forecast, the forecast period; in every other skill, the last 90 days (a review's own look-back window governs only what moved and what closes, not signals). Time-based signals such as Pushed close date count inside it. When the source holds only a lifetime push count, use that count and label it "per CRM, lifetime".
- Two-way touch: the buyer replied or attended, or a buyer-sent message that got a reply logged, or a buyer-sent message the user has logged. Opens and clicks do not count. "Involved", "engaged" and "buyer contact" in any signal or gate mean a two-way touch: the buyer replied, attended, or wrote to us.
- Valid next step: it has a date that has not passed and is either a meeting on the calendar with someone on the buyer side, or a dated task owned by either side. A calendar that covers only part of the period or only some deals is not "no calendar": each deal without any calendar entry falls back to its dated CRM next step, labelled "per CRM", and with no calendar at all every deal does. A next step with no date, or a passed date, is not valid, and No next step is then active.
- Next step that involves the buyer (Commit and Best Case gates): a meeting with someone on the buyer side, or a dated task the buyer owns. A dated CRM next step that only the seller owns meets the gate only "per CRM", and only when a buyer message in the last 14 days supports it.
- Deal quiet edge: quiet when the last two-way touch is more than N days ago. A deal with no two-way touch ever counts the days from its creation date. Zero buyer contact is Deal quiet, not Single-threaded.
- Silent champion and Deal quiet can both fire from one fact (the champion was the only buyer contact and went silent). Each is shown once as a reason. A deal's gap count counts its distinct reasons, so two signals from one fact count once.
- Past the first third of the stages: the deal's stage position, counted from the first open stage as 1, is above one third of the stage count. Use the stages in deal-lifecycle, else a supplied typical-days stage list. With no stage list, skip the stage condition and say so in the output.
- Economic Buyer: the person the buyer or a call names as approver, or who holds the approver role in buyers-and-competition `## Who buys`. When no approver role is defined there, count only a person the buyer or a call names as approver, or an executive who confirmed approval, budget or go in logged evidence. A CRM flag or contact role alone is unconfirmed until the person speaks, writes or attends; state it in the evidence as "per CRM, unconfirmed". Never overwrite a CRM role with a guess from a title.
- Champion engaged: a champion is recorded and Silent champion is not active. With no champion recorded, Silent champion cannot be tested and the deal shows a "Champion unknown" gap instead.
- Our overdue commitment: a promise needs our own statement in a call, an email or a logged summary; a CRM next step alone or a buyer request is not one. A source that was not checked cannot establish "missed", unless buyer evidence (a chase or a complaint) shows the item did not arrive. Otherwise mark the promise "unconfirmed" and keep it out of red. Counts read "N (M unconfirmed)".
- Paper process started: the buyer has asked for, sent or begun contract, legal, security or procurement work. A reference call or a budget confirmation is not paper process.
- Signing stage: the last open stage in deal-lifecycle, else the last stage in a supplied stage list.
- Open request: a buyer request not yet answered. It is a gap, never our promise.
- Weekday-only date: "by <weekday>" in a message resolves to the next such weekday after the message date (the same weekday counts as one week later). When a CRM date disagrees, show both and treat the later as the buyer's. Never turn a weekday into a CRM date.
- Gaps (an open request, Champion unknown, a missing method item) are listed as needs-attention items. Only an active risk signal makes a deal Deal at risk. A deal's reasons are its active signals plus its gaps.
- Overdue close date: an open deal whose close date has passed. It is not Slip and not a risk by itself, and it never counts in forecast categories. It is listed under Close-out candidates.
- Close-out candidates: open deals whose close date has passed (any number of days) or with no two-way touch for 60 or more days (60 is a starting value). A deal that is also Deal at risk appears in both lists, with an "Overdue close date" tag where its close date has passed.

## What counts as evidence

Evidence comes from the buyer: something they wrote, said on a call, or scheduled. A claim recorded only by our side, such as a note saying the buyer is keen, stays unconfirmed until buyer evidence supports it. Opens, clicks, and threads where only we wrote do not count as engagement. What counts as a two-way touch is defined under Definitions.

## What this file leaves out

It does not assign probabilities, weights, or numeric scores. It does not compute coverage or gaps against a target unless the team states a target in team-standards.md.

## Changelog

- 0.2.0 (YYYY-MM-DD): valid next step falls back per deal when the calendar is partial; added Weekday-only date and Open request; Our overdue commitment needs our own statement; Missed buyer promise stays unconfirmed when only our summary records it
- 0.1.3 (YYYY-MM-DD): one definition each for the period, valid next step (and the buyer-involving form for Commit and Best Case), Close-out candidates, Deal quiet edge, first third of the stages, Economic Buyer fallback, Our overdue commitment, paper process started and signing stage
- 0.1.3 (YYYY-MM-DD): Commit gate asks for a buyer-stated decision date; Silent champion and Deal quiet may fire from one fact and count once as reasons
- 0.1.2 (YYYY-MM-DD): Slip defined once (buyer-named date or Evidence date after the period); a past close date is Overdue close date, not Slip
- 0.1.2 (YYYY-MM-DD): new-deal exemption now covers Silent champion, Deal quiet, Stalled stage and Single-threaded; No next step still applies
- 0.1.2 (YYYY-MM-DD): added Definitions (within N days, two-way touch, valid next step, zero contact, Economic Buyer, champion engaged, gaps versus risk, overdue close date)
- 0.1.2 (YYYY-MM-DD): Single-threaded applies past the first third of the stages; Deal quiet covers zero buyer contact; No next step requires a valid next step
- 0.1.2 (YYYY-MM-DD): Economic Buyer, Champion and Next step axis rows aligned with Definitions; Silent champion needs a recorded champion
- 0.1.2 (YYYY-MM-DD): clean-up rule gets starting values of 60 days without a two-way touch or past the close date
- 0.1.1 (YYYY-MM-DD): downgrade signals became the single Risk signals table; added Deal quiet, No next step, Our overdue commitment; added new-deal exemption and clean-up rule
- 0.1.0 (YYYY-MM-DD): seed created
