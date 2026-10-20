---
name: mia-pack-setup
description: Builds the pack files (deal lifecycle, buyers and competition, market physics, winning plays, team standards, scoring axes, voice, working style) from the user's CRM, calls, and email. Not for judging a live pipeline (use mia-weekly-review) or for checking CRM fields (use mia-crm-data-check); say "Set up my pack", "Refresh my pack", or "Learn how I write to buyers".
---

# Pack setup

{{SHARED}}

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

Apply the person's corrections. Use real counts, stage names, and quotes (quotes with names and amounts removed), mark unsupported guesses `(inferred)`, and apply the shared file-hygiene rules to every example. A file should still be true months later. Frontmatter follows `config/SCHEMA.md`: `status: seed`, the template's current version, today's date, and on personal files `person` (the name the user gave in conversation, else "unspecified") and `role`; ask nothing extra for it. Source tags go inline in the body only. Add one Changelog line, "filled from data on <date>". Aggregates over open deals (counts, shares, types) may enter a file; names, amounts and deal-specific details may not.

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
- Company and buyer names never enter a file, for won, lost and open deals alike. Exact amounts and open-deal details never enter either.
