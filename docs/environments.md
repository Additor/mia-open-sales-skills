# Using the skills in your tool

The skills run in any AI tool that can load Agent Skills (a folder with a `SKILL.md`). What changes between tools is where your files live. Each skill checks which of two modes it is in and acts on that.

## Two modes

| | Workspace mode | Chat mode |
|---|---|---|
| Tools | Claude Code, Codex, Cursor, OpenCode, Gemini CLI, GitHub Copilot and other coding agents | Claude on the web or desktop, other chat apps |
| The skill can | Read and write files in your working folder | Read attached files and write only in the chat |
| Pack files | Written to `mia-pack/` after you confirm | Handed to you as downloads or copy blocks. You keep them in a project or attach them |
| Reports | Saved as `mia-reports/<skill>-<date>.html` (Markdown when the tool cannot show HTML) | Shown in the chat or as an artifact |
| History | The newest report in `mia-reports/` is the "previous run". Forecast snapshots go to `mia-reports/snapshots.jsonl` | None. Paste a snapshot line to give calibration history |

A skill picks the mode from the tools it has. You do not configure it.

## Where skills look for pack files

1. `mia-pack/` in the working folder.
2. Files attached to the conversation or kept in the project.
3. The `config/` templates inside the skill folder. These are defaults and count as `seed`, so the output carries the provisional line.

Edit the files in `mia-pack/`. The `config/` folders in this repository and inside each skill are templates, and changes there affect only new setups.

## Folder layout in workspace mode

```
your-project/
  mia-pack/              pack files: deal-lifecycle.md, scoring-axes.md, voice.md, ...
  mia-reports/           saved reports and snapshots.jsonl (can name deals)
```

If the project is a git repository:

- Commit the team files in `mia-pack/` so the team shares one copy and everyone sees the same versions.
- Add `mia-reports/` and your personal files (`voice.md`, `working-style.md`) to `.gitignore`.

## Install by tool

| Tool | Command or path |
|---|---|
| Any coding agent | `npx skills add Additor/mia-open-sales-skills` ([skills CLI](https://github.com/vercel-labs/skills) detects your agents; `-g` installs for all projects, `--skill <name>` picks one) |
| Claude Code, plugin | `/plugin marketplace add Additor/mia-open-sales-skills` then `/plugin install mia-open-sales-skills@mia-open-sales-skills` |
| Claude Code, manual | Copy `skills/*` to `.claude/skills/` (project) or `~/.claude/skills/` (user) |
| Codex, manual | Copy `skills/*` to `.agents/skills/` (repository) or `~/.agents/skills/` (user) |
| Cursor, OpenCode, Gemini CLI, GitHub Copilot | Project path `.agents/skills/`. Global paths differ per tool, so use the skills CLI |
| Claude on the web or desktop | Zip a folder from `skills/` and upload it as a custom skill. Install `mia-pack-setup` first |
| Any other AI tool | Paste a `SKILL.md` into the instructions and attach that folder's `config/` and `assets/` files |

Each skill folder is self-contained, so you can install one skill or all ten.

## Team setup

Leader: run `mia-pack-setup`, review the team files, set `status: reviewed`, and either commit them under `mia-pack/` in a shared repository or share the `team-pack` folder. Rep: put the team files in `mia-pack/`, then run `mia-pack-setup`, which builds only your voice and working style. Full procedure: [config/TEAM-ROLLOUT.md](../config/TEAM-ROLLOUT.md).
