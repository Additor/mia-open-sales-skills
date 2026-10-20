# Config schema

Mia Open Sales Skills read a small set of Markdown files that describe how your team sells. Together they are the pack files: a starting point you own, written in plain text, and usable in any AI tool.

This page defines the format every file follows. A skill can then find what it needs, and a team can review any change the way it reviews code.

## Files

| File | Scope | What it holds |
|---|---|---|
| deal-lifecycle.md | team | Stages, what must be true to enter and leave each one, and proof for each stage |
| scoring-axes.md | team | The categories, flags, and risk signals used to judge a deal |
| buyers-and-competition.md | team | Who buys, what we offer, how we win and lose against each competitor |
| market-physics.md | team | Patterns across closed deals and where deals stall |
| winning-plays.md | team and personal | Repeatable moves taken from won deals |
| team-standards.md | team | What every deal gets, what leaders review, handoffs |
| crm-guide.md | team | Where deals live in the CRM, which fields to update and when |
| voice.md | personal | How one person writes to buyers |
| working-style.md | personal | A person's role, best-deal moves, standing rules, and recurring slips |

## Frontmatter

Every file starts with this block.

```yaml
---
file: scoring-axes        # file name without the extension
scope: team               # team | personal
version: 1.2.0            # MAJOR.MINOR.PATCH
updated: 2026-01-31
owner: Head of Sales      # a person or a role
status: seed              # seed | reviewed
---
```

`status: seed` means the file was generated from data and nobody has confirmed it yet. The owner changes it to `reviewed` after reading it through.

Personal files carry two more fields: `person` (who the file belongs to) and `role` (`rep`, `leader`, or `both`). The role is read from working-style.md and decides which view a skill shows. Personal files are never combined into team totals, and leader outputs never quote them.

## Versioning

From version 1.0.0, raise MAJOR when an edit would change how an existing deal is classified or checked. While a file's version is below 1.0.0, such an edit raises MINOR. Raise MINOR also when something is added without changing existing results. Raise PATCH for wording. Each edit adds one line to the Changelog at the end of the file, stating what changed and why.

## Precedence

Team files set process and standards. Personal files set voice and personal habits. When the two disagree, the team file wins. The one exception is voice.md, which always belongs to the individual.

## Team rollout

The leader reviews the seeded team files, sets `status: reviewed`, raises the version and shares the team files with each rep, who keeps them unedited beside their own voice and personal plays. Changes go through the owner, who raises the version and re-shares; where two copies differ the higher version is current, and a copy more than one MAJOR version behind is reported as out of date. The detailed procedure is in TEAM-ROLLOUT.md.

## Source tags

End each factual line with where it came from: `[crm n=46]`, `[calls n=8]`, `[email n=22]`, `[stated]` for something the owner said directly, or `[inferred]` when no data backs it. A line without a tag counts as `[inferred]`.

## Type-level only

These files describe kinds of buyers and kinds of deals. They never contain buyer names, buyer companies, exact amounts (use ranges), or details of deals that are still open (aggregates over open deals, such as counts, shares and types, are fine). Competitor names are fine.

## Stamping outputs

Every skill output ends with one line naming the files it used and their versions, for example `Config: scoring-axes 1.2.0, deal-lifecycle 1.0.1`. If a file is missing, the output says so and falls back to defaults. The `Config:` line is the very last line of the output.

## Missing files

A skill still runs with no config at all. The skills' shared rules (Sources and pack files) define how a skill treats a file that does not exist ("missing") and one that exists but is unfilled ("seed", meaning `status: seed` or only template placeholders). In short, defaults fill the gap, the output says plainly where that limited the result, and a seed file's starting values stay editable.
