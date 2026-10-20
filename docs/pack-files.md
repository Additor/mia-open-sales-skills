# Pack files

Nine Markdown files in `config/` describe how your team sells. `mia-pack-setup` writes them. You review and own them. The formal schema is in [config/SCHEMA.md](../config/SCHEMA.md). Where the files live in each tool is in [environments.md](environments.md).

## The files

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

Which skill writes which file:

| Skill | Writes |
|---|---|
| `mia-pack-setup` | `deal-lifecycle.md`, `buyers-and-competition.md`, `market-physics.md`, `winning-plays.md`, `team-standards.md`, `scoring-axes.md`, `voice.md`, `working-style.md` |
| `mia-crm-data-check` | `crm-guide.md` |
| `mia-axes-calibration` | Proposes edits to `scoring-axes.md`. The owner decides |

## Rules

- **Frontmatter.** Each file declares `file`, `scope`, `version`, `updated`, `owner` and `status` (`seed` or `reviewed`). Personal files add `person` and `role`.
- **Seed and reviewed.** `seed` means data generated the file and nobody has confirmed it. The owner sets `reviewed` after reading it through. Outputs built on a seed file carry a provisional label.
- **Versioning.** Raise MAJOR when an edit changes how an existing deal is classified. Raise MINOR for additions and PATCH for wording. Below 1.0.0, a classification change raises MINOR. Add one Changelog line per edit.
- **Precedence.** Team files outrank personal files. The exception is `voice.md`, which always belongs to the individual.
- **Source tags.** Factual lines end with their origin: `[crm n=46]`, `[calls n=8]`, `[email n=22]`, `[stated]` or `[inferred]`. An untagged line counts as `[inferred]`.
- **Type-level only.** No buyer names, buyer companies, exact amounts (use ranges) or open-deal details. Competitor names are fine.
- **Stamped outputs.** The last line of every output reads like `Config: scoring-axes 1.2.0, deal-lifecycle 1.0.1`.
- **Graceful gaps.** A missing file means defaults apply and the output says so. A skill still runs with no pack files at all.

## First edit to make

`scoring-axes.md` ships with starting thresholds. Set them from your own closed deals, then run `mia-axes-calibration` to check them against last quarter.
