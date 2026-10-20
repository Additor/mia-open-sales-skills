# Contributing

## Where to edit

| Change | Edit | Then |
|---|---|---|
| Skill behavior or report layout | `src/skills/<name>.md` | Run `python3 scripts/build.py` |
| Rules shared by all skills | `src/shared/context.md` | Run `python3 scripts/build.py` |
| Pack file templates | `config/*.md` | Run `python3 scripts/build.py` |
| Output schemas, report shell, reference notes | `assets/` | Run `python3 scripts/build.py` |

Never edit `skills/` by hand. The build script deletes and regenerates it. Commit the rebuilt `skills/` folder with your source change.

## Rules for changes

1. **Keep each SKILL.md under 15 KB.** The build prints `OVER LIMIT` when a skill passes it.
2. **Version pack files.** Any edit to a file in `config/` raises its `version`, updates `updated`, and adds one Changelog line. See `config/SCHEMA.md` for the MAJOR, MINOR, and PATCH rules.
3. **Stay type-level.** Pack files never contain buyer names, buyer companies, exact amounts, or details of open deals.
4. **Name what each skill is not for.** The `description` in each skill's frontmatter says which skill to use instead. Keep that routing accurate when you add or rename a skill.
5. **Read-only by default.** A skill that writes to a CRM, inbox, or calendar asks for approval first.
6. **Add to CHANGELOG.md** for user-visible changes.

## Adding a skill

1. Create `src/skills/mia-<name>.md` with `name` and `description` frontmatter and a `{{SHARED}}` marker after the title.
2. If it produces a report, add its output schema as `assets/schemas/mia-<name>.md`.
3. Run `python3 scripts/build.py`.
4. Add a row to the skill table in `README.md`.
5. Bump the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

## License of contributions

By opening a pull request you agree to license your contribution under the AGPL-3.0-only terms in `LICENSE`.

## Reporting issues

Include the skill name, the data source you used (CRM, CSV, or a connector), the `Config:` line from the output, and what you expected.
