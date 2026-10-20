---
name: mia-pack-setup
description: Builds the starter pack files (deal lifecycle, buyers and competition, market physics, winning plays, team standards, scoring axes, voice, working style) from the user's CRM, calls, and email. Not for judging a live pipeline (use mia-weekly-review) or for checking CRM fields (use mia-crm-data-check); say "Set up my pack", "Refresh my pack", or "Learn how I write to buyers".
---

# Pack setup

## Shared rules

### Sources and pack files
Try every source (CRM, calls, email, calendar, chat, signing tool, docs, quotes) and name those that answered. Buyer chat is deal activity; check pending contracts' signing status. A CSV standing in for a CRM follows `assets/ref/shared-csv-as-crm.md`.

Read pack files by `##` heading (format in `config/SCHEMA.md`). Look in this order: the `mia-pack/` folder in the working folder, then files attached to or present in the conversation or project, then the `config/` templates, which are defaults and count as seed. Team files outrank personal ones, except voice.md. A file that does not exist is "missing": use defaults and add one closing note that pack setup can create it. A file that exists but is unfilled (`status: seed`, or only template placeholders) is "seed": use defaults for what it lacks, treat its starting values as editable (a seed scoring-axes makes categories "starting values") and add the provisional line.

### Where files live
Workspace mode: you can read and write files in the user's working folder (Claude Code, Codex, other coding agents). Chat mode: you cannot (chat apps). Pick the mode from the tools you have. In workspace mode, write pack files to `mia-pack/` only after the person confirms, save each report as `mia-reports/<skill>-<YYYY-MM-DD>.html` (Markdown when the report falls back), and state the paths. Reports can name deals, so say once to keep `mia-reports/` out of version control. In chat mode, give downloads or copy blocks and keep no history.

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

Before any file is written or draft made, read assets/ref/shared-writes.md.

This skill is read-only toward your sources. It writes nothing to a CRM and sends nothing; in workspace mode its only writes are the pack files in `mia-pack/`. It reads no pack file except to detect existing team files; `config/` templates are copied, not read as the team's pack. The person answers the opening question, at most two follow-up questions, and the confirmation, then saves the files. The opening question does not count toward the two, and the confirmation line is not a question. The reply may span several messages (summary, save, hand-off, offer); the shared one-screen limit does not apply. Anything unknown becomes an `(inferred)` mark or the words "not seen" inside a file, never an extra question in chat.

Read these reference files when the step calls for them: `assets/ref/mia-pack-setup-extraction.md` (what to pull from each source), `assets/ref/mia-pack-setup-summary.md` (how to compose the summary and the files), `assets/ref/mia-pack-setup-situations.md` (thin data, missing sources, existing team files, saving, founder handoff, refresh).

## 1. Ask one opening question

Before reading anything, ask for one or two deals the person thinks they ran well, won or lost, and say that "skip" lets you pick them. If the request was narrow (for example, only learning their writing), say in one line that the pack is a few short files and the rest needs no effort from them, then continue. If team files already sit in the project, read the situations reference first and follow it.

## 2. Find the sources

Try CRM, call recordings, email, and calendar, then chat and documents. With no source at all, follow the situations reference. Continue when sources are missing.

After each source is read, report one line such as "CRM: 143 deals, 12 won and 9 lost with notes". Skip a disconnected source with one line. Never draw a progress bar.

## 3. Read within the budget

History window: the last 6 months, widened to 12 when the total in scope is thin (fewer than 30 closed deals in the window). Closed deals inside an open-deal export count as history when they carry an outcome.

| Source | Cap |
|---|---|
| CRM deal records | 200, using aggregate queries; notes only for the best deals, the 10 most recent won, and the 10 most recent lost |
| Call transcripts in full | 3, best-deal calls first; use listed summaries freely |
| Sent emails | 25 threads to external buyers, only what is needed |
| Best deal | The full thread for up to 2 deals |

Skip long pasted digests. For a leader, add per-rep totals (deal count, conversion, days per stage) and one full deal per rep. If a source is bigger than the cap, sample the most recent and state "N of M read". Scope: a rep reads only their own deals, a leader only the team's. Decide the role with the shared rules, then use the extra signals in the extraction reference.

## 4. Study the best deals

Use the deals the person named, found in CRM, email, and calls. If they skipped, take the 2 won deals that closed fastest or largest relative to normal in the window. Read each from first touch to close, then isolate 3 to 5 behaviors that set it apart from an ordinary deal. Those feed winning-plays, working-style, the voice samples, and market-physics.

If a named deal cannot be found or is too new, say so in the summary and use the nearest deal with real history. With fewer than 2 won deals, use what exists plus the furthest-along open deal, and say so. If a rep ran the deal that counts as a leader's best, the team-level behavior is assigned to the team files, and just the leader's personal involvement is assigned to working-style.

## 5. Show the summary once

After reading, send one message that makes the person feel known. Every line must rest on something you read, and at least one line should be a pattern they probably had not noticed. A true five lines beat a padded seven. Follow the summary reference for the layout by role.

Ask at most two follow-up questions. Each points at a specific finding, can be answered in a few words, and offers your likely answer where you have one. If the role is unclear, it takes one of the two slots and the summary omits the role line. A role you stated in the summary is never asked again. Close the message with the confirmation line, which is not a question: they say "right" or fix it in a sentence. Where a source was empty, say so on the affected line with the way to connect it.

## 6. Write the files

Apply the person's corrections. Use real numbers, stage names, and quotes, mark unsupported guesses `(inferred)`, and apply the shared file-hygiene rules to every example. A file should still be true months later. Frontmatter follows `config/SCHEMA.md`: `status: seed`, the template's current version, today's date, and on personal files `person` (the name the user gave in conversation, else "unspecified") and `role`; ask nothing extra for it. Source tags go inline in the body only. Add one Changelog line, "filled from data on <date>". Aggregates over open deals (counts, shares, types) may enter a file; names, amounts and deal-specific details may not.

| File | Scope | Notes |
|---|---|---|
| deal-lifecycle | team | Use the template headings; stage conversion and days from the data |
| buyers-and-competition | team | Types only |
| market-physics | team | Counts on every pattern |
| winning-plays | team | Plays from the best deals; leave Close rate when run blank |
| team-standards | team | Fill only for leader or both; for a rep, do not create it, because the leader's copy is used |
| scoring-axes | team | Copy the template; fill only frontmatter `owner` and `updated`, and the `<amount range>` when the data supports it; the stage list goes in deal-lifecycle; `status: seed` |
| voice | personal | 1,000 to 1,800 words, real quotes included; no file when the user wrote no buyer emails (say how to add samples) |
| working-style | personal | 200 to 500 words, built from evidence only; a leader with no deals gets only the parts the evidence supports, other lines read "not seen" |

Do not create crm-guide. Say that the first run of mia-crm-data-check builds it, because reading CRM depth is costly.

## 7. Tell them where to save

Follow the saving section of the situations reference. In workspace mode, say where the files now live. In chat mode, say once, in one line, that unsaved files mean the next run starts from a seed again. For a leader, the same message also covers the team pack bundle and the rep message, per that section.

## 8. Make one offer

After saving, offer one yes-able step on real data, in the same conversation. Results carry the provisional line because the files are seeds.

- Rep: find the three deals that most need attention this week, using mia-next-move on the open pipeline.
- Leader or both: look for where the team pipeline is leaking, using mia-at-risk-review (mia-weekly-review if the first is not installed).

These two form the skill's own ordered offer. Only after the person answers it, and only when a scheduling tool exists and no Daily Sync schedule is present, offer a Daily Sync schedule in one line. Never ask both at once. The `Config:` line comes last.

## Failures and stopping

If a source fails mid-read, retry once, continue with what was read, mark totals as partial, and report the gap as an absence. A failure never blocks setup. If you must stop early, save what you have and tell the person to say "Refresh my pack" to finish.

## Rules

- Only verified lines go in the summary. When unsure, mark `(inferred)` or turn it into one of the two questions. One wrong line in the first minute breaks trust.
- Questions: the opening one, at most two follow-ups, then the confirmation.
- Open-deal names, amounts and deal-specific details never enter a file.
