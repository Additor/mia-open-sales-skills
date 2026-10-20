# Mia Open Sales Skills

<p align="center"><img src="docs/images/hero.jpg" alt="Mia Open Sales Skills: 10 free Claude skills for running a sales team. One set of written criteria for every deal." width="100%"></p>

![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue) ![Version: 0.1.0-beta.2](https://img.shields.io/badge/version-0.1.0--beta.2-orange) ![Skills: 10](https://img.shields.io/badge/skills-10-green)

Sales skills that judge every deal by the same written criteria, so your team stops arguing about what "Commit" means.

You keep the criteria as plain Markdown files. Ten skills read them and do the daily and weekly work: briefings, follow-ups, forecasts, risk reviews, CRM checks. Every report names the file versions it used.

> **Beta.** Tested on exported CSV, calendar and call data. Live CRM, email and calendar connectors are still being verified with real teams. Feedback: https://withmia.ai

## Quick start (10 minutes)

**1. Install**

```
/plugin marketplace add Additor/mia-open-sales-skills
/plugin install mia-open-sales-skills@mia-open-sales-skills
```

Other tools: see [Install](#install).

**2. Set up your pack.** Say:

```
Set up my pack
```

Answer one question, confirm what it found in your CRM, calls and email, and save the files it writes.

**3. Run something.** Say:

```
Start my Daily Sync
```

The first results carry a *provisional* label, because the pack files are drafts built from data. A leader reads them, fixes what is wrong, sets `status: reviewed`, and shares them with the team.

No CRM connection yet? Attach a CSV export of your deals and the skills treat it as the CRM.

<p align="center"><img src="docs/images/report-preview.jpg" alt="Example Daily Sync report with next moves, today's meetings, risks and a Config line, using fictional data" width="100%"></p>

## Why this exists

| Problem | What the pack does |
|---|---|
| One rep's Commit is another rep's Best Case | One `scoring-axes.md` defines Commit, Best Case, Pipeline, and the risk signals |
| Forecast calls turn into arguments about definitions | Every report applies the same definitions and prints their versions |
| Process lives in a leader's head | `deal-lifecycle.md` and `team-standards.md` write it down, in plain text you can diff |
| Reports sound confident and cite nothing | Every fact carries a source and a date. Unchecked claims read "unconfirmed" |
| Tools lock you in | The pack is Markdown. It runs in Claude and in any AI tool that reads files |

## Skills

<p align="center"><img src="docs/images/skills.jpg" alt="The ten skills grouped as Set up, Every day, Every week and Keep it honest, each with the phrase that calls it" width="100%"></p>

Each skill says what it is not for and which skill to use instead, so a plain request reaches the right one.

**Set up**

- **[mia-pack-setup](skills/mia-pack-setup/SKILL.md)**: Drafts your starter pack files from your CRM, calls and email. *"Set up my pack"*

**Every day**

- **[mia-daily-sync](skills/mia-daily-sync/SKILL.md)**: One phone-sized page with today's meetings, replies waiting, risks and next moves. *"Start my Daily Sync"*
- **[mia-meeting-prep](skills/mia-meeting-prep/SKILL.md)**: A 60-second briefing for one external meeting. *"Meeting prep for Acme"*
- **[mia-call-follow-up](skills/mia-call-follow-up/SKILL.md)**: Recap email draft, CRM change proposal and dated tasks for the call that just ended. *"Follow up on my last call"*
- **[mia-next-move](skills/mia-next-move/SKILL.md)**: One specific action and a ready-to-send message for a quiet deal. *"Next move for Acme"*

**Every week**

- **[mia-weekly-review](skills/mia-weekly-review/SKILL.md)**: Every open deal on one page, with a Team sweep and Coach's questions for leaders. *"Open my Weekly Review"*
- **[mia-forecast](skills/mia-forecast/SKILL.md)**: Commit, Best Case and Pipeline sorted from buyer evidence, set beside the CRM commit. *"Show my forecast"*
- **[mia-at-risk-review](skills/mia-at-risk-review/SKILL.md)**: Winnable deals that drifted from your own process, with a dollar figure on the gaps. *"Show deals at risk"*

**Keep it honest**

- **[mia-crm-data-check](skills/mia-crm-data-check/SKILL.md)**: Learns how your team uses the CRM, checks open deals against it, and prepares fixes for approval. *"Check my CRM data"*
- **[mia-axes-calibration](skills/mia-axes-calibration/SKILL.md)**: Replays your scoring criteria on closed deals and proposes edits where outcomes disagree. *"Calibrate my axes"*

## How it works

<p align="center"><img src="docs/images/how-it-works.jpg" alt="Four steps: read your data, draft nine pack files with mia-pack-setup, review and version them, run the ten skills" width="100%"></p>

1. `mia-pack-setup` drafts nine Markdown **pack files** that describe how your team sells: stages, buyers, competitors, scoring criteria, voice, standing rules.
2. You and your team review and version them like code.
3. The other skills read those files and end every output with a `Config:` line. Two people with different version numbers know their copies have drifted.

Pack files hold type-level descriptions only. They contain no buyer names, no exact amounts and no open-deal details. File list, frontmatter, versioning and precedence rules: [docs/pack-files.md](docs/pack-files.md).

## Install

| Where | How |
|---|---|
| Claude Code, marketplace | `/plugin marketplace add Additor/mia-open-sales-skills` then `/plugin install mia-open-sales-skills@mia-open-sales-skills` |
| Claude Code, manual | `git clone https://github.com/Additor/mia-open-sales-skills.git` then `cp -r mia-open-sales-skills/skills/* ~/.claude/skills/` (or `<project>/.claude/skills/`) |
| Claude on the web or desktop | Zip a folder from `skills/`, for example `skills/mia-daily-sync`, and upload it in Settings under Skills. Install `mia-pack-setup` first |
| Any other AI tool | Paste a skill's `SKILL.md` into the instructions and attach that folder's `config/` and `assets/` files. Each `SKILL.md` stays under 15 KB |

Each folder in `skills/` is self-contained, so you can install one skill or all ten. While the repository is private, Claude Code needs a GitHub login that can read it.

## Team rollout

1. The leader runs `mia-pack-setup`, reads the six team files, fixes them, and sets `status: reviewed`.
2. The leader shares them as one `team-pack` folder and posts the current version of each file.
3. Each rep adds the folder beside their own files and runs `mia-pack-setup`, which builds only their voice and working style.
4. A rep who disagrees with a criterion sends the leader the file, the reason and the deals affected. Team files are never edited locally.

Full procedure: [config/TEAM-ROLLOUT.md](config/TEAM-ROLLOUT.md).

## Customize

| To change | Edit |
|---|---|
| Thresholds, categories, risk signals | `config/scoring-axes.md` |
| Stages and entry conditions | `config/deal-lifecycle.md` |
| Team rules and weekly review items | `config/team-standards.md` |
| How drafts sound | `config/voice.md` |
| What a skill does, or a report layout | `src/skills/<name>.md`, then `python3 scripts/build.py` |

Never edit `skills/` by hand. The build regenerates it. Raise the file version and add a Changelog line with each pack file edit.

## Safety and privacy

- Report skills are read-only. They never send, post or write to your CRM.
- Skills that propose changes (`mia-call-follow-up`, `mia-crm-data-check`) wait for your explicit approval.
- Skills run when you call them and read only the sources you connect.
- Reports make no network request when they open. A footer may carry one link to the Sales AQ check, with a campaign tag and no deal data, followed only if you click it.
- Reports describe work, not people: no scores, rankings or personal adjectives for reps.

## Known limits

The free pack cannot force a team onto the same files. Each person holds a copy, and copies drift. The `Config:` line is how you notice. Files also go stale, and reviews run only when someone asks. [Mia](https://withmia.ai) is the hosted option for teams that outgrow the manual routine: one shared source, scheduled runs, and account-level memory.

## Contributing

Issues and pull requests are welcome. Setup, repository layout and rules: [CONTRIBUTING.md](CONTRIBUTING.md). Release notes: [CHANGELOG.md](CHANGELOG.md).

## License

[AGPL-3.0-only](LICENSE). Copyright 2026 Withmia.

- Use it inside your company freely.
- If you distribute a modified copy, or run one as a hosted service for others, publish your modified source under the same license.
- Pack files and reports you generate from your own data are your content.

The LICENSE file is the binding text.
