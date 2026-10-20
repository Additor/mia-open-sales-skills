---
name: mia-axes-calibration
description: Replays the criteria in scoring-axes.md on closed deals, using evidence from 30 days before each close, and proposes edits where the criteria and outcomes disagree. Not for writing the criteria the first time (use mia-pack-setup) or for forecasting open deals (use mia-forecast); say "Calibrate my axes", "Do my criteria hold up on last quarter?", or "Replay my scoring on closed deals".
---

# Axes calibration

## Shared rules

### Sources and pack files
Try every source (CRM, calls, email, calendar, chat, signing tool, docs, quotes) and name those that answered. Buyer chat is deal activity; check pending contracts' signing status. A CSV standing in for a CRM follows `assets/ref/shared-csv-as-crm.md`.

Read pack files by `##` heading (format in `config/SCHEMA.md`). Look in this order: the `mia-pack/` folder in the working folder, then files attached to or present in the conversation or project, then the `config/` templates, which are defaults and count as seed. Team files outrank personal ones, except voice.md. A file that does not exist is "missing": use defaults and add one closing note that pack setup can create it. A file that exists but is unfilled (`status: seed`, or only template placeholders) is "seed": use defaults for what it lacks, treat its starting values as editable (a seed scoring-axes makes categories "starting values") and add the provisional line.

### Where files live
Workspace mode: you can read and write files in the user's working folder (Claude Code, Codex, other coding agents). Chat mode: you cannot (chat apps). Pick the mode from the tools you have. In workspace mode, write pack files to `mia-pack/` only after the person confirms, save each report as `mia-reports/<skill name>-<YYYY-MM-DD>.html` (for example `mia-weekly-review-2026-10-20.html`; Markdown when the report falls back), and state the paths. Reports can name deals, so say once to keep `mia-reports/` out of version control. In chat mode, give downloads or copy blocks and keep no history.

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

Before step 1, read assets/ref/shared-reports.md.

This skill is read-only. It proposes edits to scoring-axes.md and changes nothing until the person approves a diff. In workspace mode it then writes the edited file to `mia-pack/scoring-axes.md` with the version bump and the Changelog line; in chat mode the person saves the file themselves. Run it after a quarter closes or before changing the criteria. Read `assets/schemas/mia-axes-calibration.md` for the report layout.

## Where history comes from

Snapshot lines come from earlier mia-forecast runs. In workspace mode mia-forecast appends them to `mia-reports/snapshots.jsonl`: read that file first. In chat mode nothing is stored, so use snapshot lines the person pastes and say plainly that none are kept. Without snapshots, reconstruct.

## Sample gate

Full run: 20 closed deals with at least 5 won and 5 lost. Read at most 100, most recent first, within the view and scope set by the shared rules (a leader reads the team's deals, a rep their own). Below that, never end on a bare refusal:

- A personal scope below the minimum: say how many closed deals it holds and offer the team scope or a pasted team CSV.
- 8 or more closed deals but below the full minimum (under 20, or under 5 won, or under 5 lost): run a directional replay. Build the report with the replay and the Signals, leave Proposed edits on its empty text, and say how many more closed deals, and of which outcome, a full run needs.
- Fewer than 8 closed deals: build no report. Say how many more are needed and what to bring: a CSV of closed deals from the past 12 months with stage, amount, created date, close date and outcome.

## Procedure

1. Rebuild the evidence for each closed deal as it stood 30 days before the close. Use only calls, email, calendar, and CRM activity dated before that point. If stage history is missing, use activity alone and say that limit applies. A saved snapshot replaces this step for the deals it covers.
2. Classify each deal with the gates and signals now in scoring-axes.md: Commit, Best Case, or Pipeline, plus which Risk signals were active.
3. Compare with what happened:
   - deals classed Commit that were lost;
   - deals outside Commit and Best Case that were won;
   - signals active as often on won deals as on lost ones;
   - signals that never fired;
   - how classification would change if a threshold moved (for example, Deal quiet from 14 to 21 days).
4. For each disagreement pattern, draft an edit to scoring-axes.md: current value, proposed value, and the number of deals supporting it ("Backed by N deals": the deals where the edited signal fires). Mark the edit weak when fewer than 8 deals support it.
5. State the version bump each edit needs under `config/SCHEMA.md`: MAJOR if it changes how an existing deal is classified (from 1.0.0; while the file's version is below 1.0.0 such an edit raises MINOR), MINOR if it only adds, PATCH for wording.

Never create or suggest probabilities, weights, or scores. Describe deals and criteria, never people.

## Lifetime replay

When closed-deal data holds only lifetime summaries with no dates (a CSV export, say), run a lifetime replay, which is a partial replay. Test only the signals the data can test and label every result "per CRM, lifetime". State that the 30-day cutoff was not enforced. Classify each closed deal on the gates that can be tested ("Commit on testable gates") and say so. Tag a signal the data cannot test "Not testable" and name it in the limits section, not in `howBuilt`. A competitor name with no date or preference is not testable for Competitor mention.

## Hard rules

- Classify from evidence dated at least 30 days before the close, except in a lifetime replay. Never use anything learned after that point.
- Every edit is backed by a deal count.
- The file does not change until the person approves the diff.
- Saved files never receive buyer details; the report may name deals.

## Report

Sections, in fixed order: Replay summary; Where the criteria disagreed with outcomes; Signals; Proposed edits; What this run cannot conclude. Header numbers: closed deals analyzed, won, lost, how many came from snapshots, and how many were reconstructed. If snapshots and reconstruction were mixed, name which deals used which in `howBuilt`. In chat mode, when approved edits are saved, tell the person to add one line to the Changelog in scoring-axes.md and raise the version as stated.

## Chat reply

Layout: how many closed deals were analyzed and the split by outcome; the single largest place where criteria and outcomes disagreed; the one edit that would change the most results; the sources line (what was read, what was not connected). Offer: the full scoring-axes.md with the proposed edits applied, for the person to save. Make no other offer.

## Special cases

- Fewer than 20 closed deals, or fewer than 5 of either outcome: follow the sample gate tiers above.
- No call or email history: activity will be thin and most deals will fall into Pipeline. Say so and mark conclusions weak.
- Lost deals with no loss reason: say so once, in the report's limits section.
- Mixed snapshot and reconstruction: record in `howBuilt` which deals used which.
- Seed status on scoring-axes: the criteria are placeholder values, so expect disagreement. Call the categories "starting values" as the shared rules require.
