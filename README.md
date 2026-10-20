# Mia Open Sales Skills

![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue) ![Version: 0.1.0-beta.2](https://img.shields.io/badge/version-0.1.0--beta.2-orange) ![Skills: 10](https://img.shields.io/badge/skills-10-green)

Ten free, open-source AI skills that let a sales team judge every deal by the same written criteria.

You keep the criteria as plain Markdown files, edit them as your process changes, and every report prints the file versions it used. The skills run in Claude and in any AI tool that can read files.

> **Status: 0.1.0-beta.2.** Tested on exported CSV, calendar and call data. Live connector paths (CRM, email, calendar) and marketplace install are still being verified with real teams. Send feedback to the Withmia team via https://withmia.ai.

## Contents

- [What this is](#what-this-is)
- [Quick start](#quick-start)
- [Install](#install)
- [The ten skills](#the-ten-skills)
- [How the pack files work](#how-the-pack-files-work)
- [Team rollout](#team-rollout)
- [Customizing](#customizing)
- [Repository layout](#repository-layout)
- [Privacy](#privacy)
- [Limits of the beta](#limits-of-the-beta)
- [Contributing](#contributing)
- [License](#license)

## What this is

Most teams judge deals by gut feel, and each rep uses a different bar. A deal one rep calls Commit looks like Best Case to the next rep. Forecast calls turn into arguments about definitions.

This pack fixes the definitions first, then runs the daily and weekly sales work against them.

1. **Pack files** in `config/` describe how your team sells: stages, buyers, competitors, scoring criteria, voice, standing rules. A setup skill drafts them from your CRM, call recordings, and inbox.
2. **Ten skills** read those files and do the work: morning briefing, meeting prep, call follow-up, forecast, at-risk review, CRM hygiene, and more.
3. **Every output ends with a `Config:` line** that lists the files and versions used. Two people with different numbers know their files have drifted.

The pack files are type-level descriptions. They hold no buyer names, no exact amounts, and no details of open deals.

## Quick start

1. [Install the pack](#install).
2. Say **"Set up my pack"**. Answer one question, confirm what it found, and save the files it creates.
3. Say **"Start my Daily Sync"** or **"Open my Weekly Review"**.

The first results carry a *provisional* label, because the pack files are still starting points drafted from data. If you lead a team, read each file, fix what is wrong, set `status: reviewed`, and share the files with your reps (see [Team rollout](#team-rollout)).

You do not need a CRM connection to try it. Attach or paste a CSV export of your deals and the skills treat it as the CRM (`assets/ref/shared-csv-as-crm.md`).

## Install

### Claude Code (plugin marketplace)

```
/plugin marketplace add Additor/mia-open-sales-skills
/plugin install mia-open-sales-skills@mia-open-sales-skills
```

While the repository is private, Claude Code needs a GitHub login that can read it.

### Claude Code (manual copy)

Each folder in `skills/` is self-contained, with its own `config/` and `assets/`. Copy the ones you want:

```bash
git clone https://github.com/Additor/mia-open-sales-skills.git
cp -r mia-open-sales-skills/skills/* ~/.claude/skills/      # all users
# or: cp -r mia-open-sales-skills/skills/* <your-project>/.claude/skills/   # one project
```

### Claude on the web or desktop

Zip a folder from `skills/` (for example `skills/mia-daily-sync`) and upload it under Settings, Capabilities, Skills. Repeat for each skill you want. Install `mia-pack-setup` first.

### Any other AI tool

Paste a skill's `SKILL.md` into the tool's instructions and attach the files from that skill folder's `config/` and `assets/`. A SKILL.md is up to 15 KB, so pick a tool that accepts long instructions or file uploads.

## The ten skills

| Skill | Say | What you get |
|---|---|---|
| [mia-pack-setup](skills/mia-pack-setup/SKILL.md) | "Set up my pack" | Starter pack files drafted from your CRM, calls, and email |
| [mia-daily-sync](skills/mia-daily-sync/SKILL.md) | "Start my Daily Sync" | One phone-sized page: today's meetings, replies waiting, risks, next moves |
| [mia-meeting-prep](skills/mia-meeting-prep/SKILL.md) | "Meeting prep for Acme" | A 60-second briefing for one external meeting |
| [mia-call-follow-up](skills/mia-call-follow-up/SKILL.md) | "Follow up on my last call" | Recap email draft, CRM change proposal, and dated tasks. CRM writes wait for your approval |
| [mia-next-move](skills/mia-next-move/SKILL.md) | "Next move for Acme" | One specific action and a message ready to send for a quiet deal, or a ranked scan of the pipeline |
| [mia-weekly-review](skills/mia-weekly-review/SKILL.md) | "Open my Weekly Review" | Every open deal on one page: what moved, what is at risk, what closes. Leaders also get a Team sweep and Coach's questions |
| [mia-forecast](skills/mia-forecast/SKILL.md) | "Show my forecast" | Commit, Best Case, and Pipeline sorted from buyer evidence, set beside the CRM commit |
| [mia-at-risk-review](skills/mia-at-risk-review/SKILL.md) | "Show deals at risk" | Winnable deals that drifted from your own process, with a dollar figure on the gaps |
| [mia-crm-data-check](skills/mia-crm-data-check/SKILL.md) | "Check my CRM data" | Learns how your team uses the CRM, checks open deals against that guide, and prepares fixes for approval |
| [mia-axes-calibration](skills/mia-axes-calibration/SKILL.md) | "Calibrate my axes" | Replays your scoring criteria on closed deals and proposes edits where the criteria and the outcomes disagree |

Each skill states what it is not for and which skill to use instead, so the right one triggers from a plain request.

### Which skill, when

| Moment | Skill |
|---|---|
| First day, or after your process changes | mia-pack-setup |
| Start of the working day | mia-daily-sync |
| Before a buyer meeting | mia-meeting-prep |
| Right after a call | mia-call-follow-up |
| A deal went quiet | mia-next-move |
| Monday pipeline review or 1:1 | mia-weekly-review |
| Forecast call | mia-forecast |
| Looking for leaks in the pipeline | mia-at-risk-review |
| Messy CRM | mia-crm-data-check |
| Once a quarter | mia-axes-calibration |

### Safety defaults

- Report skills are read-only. They do not send email, post messages, or write to the CRM.
- Skills that propose changes (`mia-call-follow-up`, `mia-crm-data-check`) wait for your explicit approval before writing anything.
- Every fact in a report carries its source and date. A claim with no evidence reads "unconfirmed" or "not seen".
- Reports describe work, not people. They give no scores, rankings, or personal adjectives for reps.

## How the pack files work

Nine Markdown files in `config/` describe how your team sells.

| File | Scope | Holds |
|---|---|---|
| `deal-lifecycle.md` | team | Stages, entry and exit conditions, proof for each stage |
| `scoring-axes.md` | team | Categories (Commit, Best Case, Pipeline), flags, risk signals, definitions |
| `buyers-and-competition.md` | team | Who buys, what you offer, how you win and lose against each competitor |
| `market-physics.md` | team | Patterns across closed deals and where deals stall |
| `winning-plays.md` | team and personal | Repeatable moves taken from won deals |
| `team-standards.md` | team | What every deal gets, what leaders review weekly, handoffs |
| `crm-guide.md` | team | Where deals live in the CRM and which fields to update when |
| `voice.md` | personal | How one person writes to buyers |
| `working-style.md` | personal | Role (rep, leader, both), standing rules, recurring slips |

Rules that keep the files trustworthy:

- **Frontmatter.** Each file declares `scope`, `version`, `updated`, `owner`, and `status` (`seed` or `reviewed`).
- **Versioning.** Raise MAJOR when an edit changes how an existing deal is classified. Raise MINOR for additions, PATCH for wording. Add one Changelog line per edit.
- **Precedence.** Team files outrank personal files. The exception is `voice.md`, which always belongs to the individual.
- **Source tags.** Factual lines end with their origin: `[crm n=46]`, `[calls n=8]`, `[email n=22]`, `[stated]`, or `[inferred]`.
- **Stamped outputs.** The last line of every output reads like `Config: scoring-axes 1.2.0, deal-lifecycle 1.0.1`.
- **Graceful gaps.** A missing file means defaults apply and the output says so. A `seed` file means starting values apply and the output is labelled provisional.

The full format is in [config/SCHEMA.md](config/SCHEMA.md).

The criteria in `scoring-axes.md` start with placeholder values. Replace them with numbers from your own closed deals, then run `mia-axes-calibration` to check them.

## Team rollout

1. The leader runs `mia-pack-setup` and reads the six team files it writes.
2. The leader fixes what is wrong, sets `status: reviewed`, and raises the versions.
3. The leader shares the files as one `team-pack` folder or zip, and posts the current version of each file.
4. Each rep drops the folder next to their own pack files and runs `mia-pack-setup`. It builds only their `voice.md` and `working-style.md`.
5. A rep who thinks a criterion is wrong sends the leader the file name, the reason, and the kind of deals affected. Nobody edits team files locally.

Step-by-step detail is in [config/TEAM-ROLLOUT.md](config/TEAM-ROLLOUT.md).

## Customizing

| You want to change | Edit |
|---|---|
| Thresholds, categories, risk signals | `config/scoring-axes.md` |
| Stages and their entry conditions | `config/deal-lifecycle.md` |
| Team rules and weekly review items | `config/team-standards.md` |
| How drafts sound | `config/voice.md` |
| What a skill does or how it lays out a report | `src/skills/<name>.md`, then run `python3 scripts/build.py` |

Do not edit the generated files in `skills/`. `scripts/build.py` rebuilds each `skills/<name>/SKILL.md` from `src/skills/<name>.md`, inserts the shared rules from `src/shared/context.md`, and copies the matching `config/` and `assets/` into each skill folder. It warns when a SKILL.md passes 15 KB.

## Repository layout

```
.claude-plugin/       Plugin and marketplace manifests
skills/               Built skills, one self-contained folder each (SKILL.md, config/, assets/)
src/skills/           Skill sources, edit these
src/shared/context.md Shared rules inserted into every skill
config/               Pack file templates and the schema
assets/               Report shell (HTML), output schemas, reference notes
scripts/build.py      Builds skills/ from src/
```

## Privacy

- Skills run when you call them and read only the sources you connect.
- Reports make no network request when they open.
- A report footer may carry one link to the Sales AQ check, with a campaign tag and no deal data. It is followed only if you click it.
- Pack files hold type-level descriptions. Review them before you share them outside your team.

## Limits of the beta

- The free pack cannot force everyone onto the same files. Each person holds a copy, and copies can drift. The `Config:` line on every output is how you notice.
- Live connector paths and marketplace install are still being verified.
- Files go stale and reviews happen only when someone asks for them. A hosted setup with account-level memory and scheduled runs is what [Mia](https://withmia.ai) provides for teams that outgrow the manual routine.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Edit `src/` and `config/`, run `python3 scripts/build.py`, and commit the rebuilt `skills/` folder with your change.

## License

GNU Affero General Public License v3.0 only (`AGPL-3.0-only`). See [LICENSE](LICENSE) and [NOTICE](NOTICE).

In practice:

- **Use it inside your company, freely.** Install the skills, edit the pack files, and run them on your own deals. No obligation arises from internal use.
- **Share your changes if you share the pack.** If you distribute a modified copy, or offer a modified version to others as a hosted service over a network, you must publish your modified source under the same license.
- **Keep the notices.** Copies must carry the LICENSE and NOTICE files.
- **Your data stays yours.** The license covers the files in this repository. Pack files and reports you generate from your own CRM, calls, and email are your content.

This summary is a convenience. The LICENSE file is the binding text.

Copyright 2026 Withmia (withmia.ai).
