---
name: mia-crm-data-check
description: Learns how the team really uses its CRM, saves that as crm-guide.md, then checks open deals against the guide and prepares fixes for approval. Not for the one call that just ended (use mia-call-follow-up) or for judging deal health (use mia-at-risk-review); say "Check my CRM data", "Refresh my CRM guide", or "Move <deal> to Proposal and note 40 seats".
---

# CRM data check

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

Before step 1, read assets/ref/shared-reports.md. Before any draft or change, read assets/ref/shared-writes.md.

Works with any CRM or a CSV. Read-only until a change is approved. The only answers needed are one guide confirmation (guide-build run) and one approval per change group.

Read when needed: `assets/ref/mia-crm-data-check-guide-build.md` (building and saving the guide), `assets/ref/mia-crm-data-check-checks.md` (rules for each category), `assets/ref/mia-crm-data-check-situations.md` (missing sources, large CRMs, intentional blanks). The report layout is `assets/schemas/mia-crm-data-check.md`.

## Modes

1. Guide build: no crm-guide.md exists, so this run creates it.
2. Check: report field status and counts, then prepare fixes.
3. Plain-language update: the person describes a change in words and you turn it into field changes.

A single call that just ended belongs to mia-call-follow-up; say so and stop.

## Step 1: Find the guide

Look for crm-guide.md in the project and read deal-lifecycle (`## Pipelines and stages`, `## Qualification to close`), team-standards (`## Every deal gets`) and scoring-axes (`## Definitions`). With a guide present, go straight to the check. When the CRM has changed since (a field or stage the guide names is missing, or a pipeline has appeared), put a one-line note first and suggest "Refresh my CRM guide". With no guide, build one (Step 2). If a guide was built earlier in this conversation but is not in the project, rebuild it and remind the person once to save it. A scope named in the request wins over the inferred view.

## Step 2: Build the guide (guide-build run only)

Say in one line that the guide is being built, that it takes a few minutes, and that one confirmation follows. Follow the guide-build reference. Pull as many as 200 deals, meaning open ones along with those closed during the previous 6 months, using aggregate queries instead of reading each record; look at calls and email solely where a stage moved. Ask at most one question in a single confirmation message, save the guide with the `config/crm-guide.md` headings in template order, then go straight to Step 3 in the same turn.

## Step 3: Check the deals

Finish in one conversation. When sampling, state it ("checked the 200 most recently active of about 640 open deals") and use the same set every run so weeks compare.

| Source | Cap |
|---|---|
| Open deals in scope | 200, taking the guide's fields along with company, contacts, last activity, stage and owner |
| Tasks and meetings | Open tasks and future meetings on those deals (valid next step per scoring-axes `## Definitions`; a deal with no calendar entry falls back to its dated CRM step, "per CRM") |
| Calls | Summaries dated within 30 days, for deals in scope (about 20 per pull); complete transcripts for no more than 3, and only when a summary points to a rival, an unfamiliar person, or a figure |
| Email | 25 recent threads with in-scope contacts |
| Duplicates | Up to 500 records: companies and contacts on in-scope deals that were added during the past 90 days |

Also note calls with companies that have no open deal and calls with deals closed lost. For a single named deal, check only it and read all its calls and email. A leader's sample is proportional by rep; use filtered counts for totals where they exist.

Run the seven categories in the checks reference. Check against the team's guide, not a generic list. When two guide rules clash, the more specific wins; note the clash in one line. If one rule drags a count down (a "two contacts" rule failing 22 deals), say so in the category detail with the count without it; never ask in chat.

## Step 4: Report

Follow the schema file; the section order is fixed. Status per category is OK or Needs attention with a count, such as "29 of 41 pass". No scores and no overall average. A category that could not be checked reads "not checked" with the reason. Every count shows its n.

Fixes carry evidence and steps. Order by deal amount, largest first, then soonest close date; the display opens with the first 8 (6 for a team view), the rest after, grouped by owner. Merges go under Duplicates, never in Fixes.

## Chat reply

Short; approval happens here.
1. Deals checked, and the biggest problem.
2. A header with the number of fixes drawn from calls and email (every fix whose source is a call or a logged email), then one line per fix: deal, field, old value, new value, evidence (source and date). Include links to existing contacts (one person per line, deal and owner first) and new tasks with date and owner.
3. One line on the other groups ready (next-step and close-date fixes, stage moves) and how many decisions need an owner.

Sort the fixes into 10 groups at most, titling each by its purpose (say "Call and email fixes", "Next step and close date updates", "Stage moves"); titles never say "batch" or carry a number. List only the first group line by line; name the rest, and every named fix must appear in a later group or the copy list. Groups hold only changes ready to apply. Decisions go to Open decisions, by owner for a leader. A fix without a source is a guess: drop it or move it to Open decisions. On a first run (no earlier report), add a line that the same page appears every time and its footer explains the categories; a guide-build run also says the guide was built this run. Record any read cap hit in `howBuilt`.

## Step 5: Apply approved changes

Confirm a write tool exists (update or edit, not only search and read). If so, end the report offering the N changes, with "go ahead" or "go ahead, but skip <Deal>" as replies. Without one (a CSV counts as none), the copy list is its own file, grouped by deal: field and new value, contacts to add, tasks with dates; when files cannot be made, it is a chat block. The chat shows only the first group line by line.

Apply only the approved group, exactly as shown, nothing added. Apply one group at a time even if several were approved, and stop and ask if any change fails. If a group was only named and the person says "do all of them", show its exact lines first and confirm. Once the write is done, fetch every record again and report the outcome in everyday language instead of IDs or field codes: "✓ <Deal> · <what changed>" or "✗ <Deal> · <what did not save> (<reason>)". Then name the next group. Never merge, delete, or change an owner, even if told to do everything; explain how to do it in the CRM.

## Plain-language update

Turn the request into exact field changes with the guide's Fields by moment and Required fields. Fill what calls and email already answer, ask only for a field the new stage requires that you cannot find, show the changes, and apply on "yes". If the evidence falls short of the new stage, say that in one line and leave the choice to the person.

## Step 6: Close

Each run carries one offer answerable with yes, placed after the final apply message, or after the report when nothing can be applied or the CRM is not writable. The report already ends on the "make these changes" question, so add no second question there. When a scheduling tool exists but no CRM check is scheduled, offer to have the check ready before the weekly pipeline review; should the calendar contain a repeating pipeline or forecast meeting (or the regular sales meeting), name that meeting and suggest a slot one to two hours before it (for a 10:00 Monday review, 8:00). A yes schedules it at the time the person picks. Otherwise offer Weekly Review on the cleaned data, or a Next move for the deal with the largest amount among those without a valid next step.

## Rules

- A wrong CRM value is worse than an empty one, because everyone trusts it. Nothing is written before approval.
- Every fix has evidence a person can approve without opening anything.
- Never guess a date, amount, or stage. Without evidence, ask.
- Check against the guide; never flag a field the team does not use.
- Saved files hold fields, stages, timing, and rules only; the report may name deals.
- Every count has an n; unchecked categories stay out of totals.
