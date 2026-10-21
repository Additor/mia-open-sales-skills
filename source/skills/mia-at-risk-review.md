---
name: mia-at-risk-review
description: Finds the winnable deals that have drifted from the team's own process, puts a dollar figure on the gaps, and measures how closely the team keeps its winning habits. Not for a full pipeline page (use mia-weekly-review), a Commit and Best Case breakdown (use mia-forecast) or the next message on one deal (use mia-next-move); try "Show deals at risk", "Where are we leaking?" or "What am I missing in my pipeline?"
---

# At-risk Review

{{SHARED}}

Before step 1, read assets/ref/shared-reports.md. Before any draft, read assets/ref/shared-writes.md.

## Purpose
Hold the open pipeline against the team's own way of selling: "the team says it does X, and here it did not happen." It covers the gaps found, the dollars attached to each, and the actions open this week. It is not a pipeline review. Read-only: write nothing to the CRM, send nothing, and create no drafts in anyone's inbox before the user approves. Ask no scoping questions unless truly unclear.

## View
Apply the view rules. A rep or solo seller sees own open deals. A leader sees the team's open deals rolled up by rep (a leader who owns deals counts as one rep). For both: "my deals", "what am I missing" or "my pipeline" means own deals, with one closing line offering the team view; "our team", "where are we leaking" or the bare trigger phrase means the team view with the user's deals as one rep. A leader with no deals always gets the team view. If unsure, show own deals and offer the team version. Cover every live sales pipeline, each labelled.

## Standard
A gap is meaningless without a yardstick, so fix the yardstick before anything else and record it in `measuredAgainst`:
1. Pack files: team-standards (`## Every deal gets`, `## Working rules`), deal-lifecycle (`## Pipelines and stages` conditions, `## Qualification to close`), working-style (`## Standing rules`, `## Moves from my best deals`, `## Recurring slips`). Risk and its terms come from scoring-axes (`## Risk signals`, `## Definitions`).
2. For missing or seed files (shared definitions), infer from the CRM (stage names, required fields, method fields) and use the default habits listed in the habits reference below, saying so.

For a rep on a team, the standard comes from the leader's shared files, habits come from the rep's personal working-style, and colleagues' deals stay out of view.

## Read budget
When sampling, state it ("activity read on the 40 biggest of 130 deals").
- CRM: all open deals in scope by filtered list query (stage, amount, close date, owner, created date, last activity, next step and date, contact count, method fields), up to 150.
- Contacts and activity (emails, meetings, notes, tasks): up to 40 deals, largest and nearest-closing first.
- Habit measurement: up to 20 deals won in the last 6 months (summary fields only).
- Calls: summaries and action-item lists from the last 30 days; full text for at most 3 calls, only where a summary hints at a promise it cannot confirm.
- Email: up to 40 threads of outbound mail to buyer domains, from the past 30 days, only where a call occurred or a promise was made. Also scan every inbound external email from the last 14 days, from any sender and including shared inboxes, for questions or requests nobody answered, up to 30 threads. With a shared inbox, list conversations open or unassigned over the previous 14 days; with a personal inbox, look for inbound external threads with no later reply. Complaints and cancellations often come from people with no open deal.
- Before declaring a follow-up "missed", search every place it could have gone: each linked email account or team inbox, emails attached to the CRM deal, and chat. Say which sources could and could not be checked.
- Calendar: outside-party meetings from the past 30 days plus the coming 14, linked to deals through the attendee's email domain.
- Leaders: repeat this per rep, at most 15 activity reads per rep, with totals covering the rest.

## Part 1: find the gaps
Read `assets/ref/mia-at-risk-review-gap-checks.md` and run every check on every in-scope deal, keeping a dated, quoted or counted piece of evidence per gap. The file also defines the red, gold and green classification, ordering and headline numbers. Gaps are listed as "Needs attention" (the Off-process section), separately from red; only an active risk signal makes a deal red.

## Part 2: check the habits
Read `assets/ref/mia-at-risk-review-habits-and-cases.md` (it also lists the default habits) and measure 3 to 5 habits as counts over the last 30 to 90 days ("recap sent within a day after 4 of 13 demos"), drawing on the pack files, else on up to 20 recent wins (marked "Inferred from wins"), else on the default habits. Habits are about the work, never people.

## This week
Pick 3 to 5 actions ranked by money and time sensitivity. Each is a concrete action on a named deal or habit for this week ("send the pricing promised on the 12th today"), never "improve follow-up". In team view name the owning rep, and make at least one action a team habit to raise at the next team meeting.

## Sections, in this order
Read `assets/schemas/mia-at-risk-review.md` before filling DATA. Put the `measuredAgainst` line in the `note` of the first section; the schema defines what else that note holds.
1. Header numbers: amount at risk, amount gone quiet, unkept promises this month as "N (M unconfirmed)".
2. Habits.
3. Team sweep (team view only).
4. Deals at risk (up to 40, biggest and most urgent first).
5. This week.
6. What's working: 2 to 4 items (a habit kept, a deal moved, a promise kept fast), so the page is not only bad news.
7. Off-process, the "Needs attention" gaps (up to 40).
8. Promises.
9. Buyer conversations with no deal.
10. Close-out candidates (scoring-axes `## Definitions`); up to 5, largest first. A candidate that is at risk also keeps its row in Deals at risk, tagged "Overdue close date" where its close date has passed; one that is not at risk appears here only, not in Off-process, and not in the header amounts.
11. On track (count and names only).

Use the shell's `cap` and `children` for size. Personal view shows 8 at-risk and 8 off-process deals and counts the remainder. Team view shows one line per rep in the Team sweep, with a gap count (each deal's distinct reasons per scoring-axes `## Definitions`, summed per rep, counts only), and only the 6 largest at-risk deals; per-rep habit bars appear only when a row is opened if there are more than 6 reps. Spell owner names identically.

## Special situations
Read `assets/ref/mia-at-risk-review-habits-and-cases.md` for missing CRM, CSV, call, email or pack file, a failed source, thin data.

## Chat reply

Layout: key numbers: amount and count at risk, amount gone quiet, unkept promises this month as "N (M unconfirmed)". Top items: 3 actions for this week (action, deal, why now) and the weakest habit as "N of M"; team view adds one line per rep with amount at risk and weakest habit. Sources line: what was checked and what was not, for example "chat not connected, 2 promises unconfirmed". A clean pipeline gets one line saying so.

Offer: a follow-up draft for the largest gap that carries a promised item ("Draft the follow-up to Tallow Freight with the pricing promised on June 12?"); when the biggest-dollar gap has no such item, take the largest one that does. With none, a leader gets a note to a rep about one deal, anyone else the shared priority. Draft only, in the user's voice when it is written as them. This draft is the skill's own offer; the schedule offer (a Monday 8:00 run, with a few words on what a scheduled task is) comes only in the reply after the user answers, under the shared rules.

## Rules
- Flag only what was checked: telling someone they did not send what they did send ruins the page. An unchecked source yields "unconfirmed".
- Use the team's standard, in their stage names, method and rules, not a generic one.
- Money and dates, not adjectives: every red row has an amount, a date and a count.
- Fair to reps: describe work ("no recap after 6 of 9 demos"), credit habits kept, never write about the person.
- Anything the report carries forward for a later comparison holds counts and habits only, never buyer names, companies or exact amounts.
- Deal names are company names. Every action carries 2 to 4 verb-first steps.
