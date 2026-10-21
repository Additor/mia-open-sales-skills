# Contributing

## Repository layout

```
skills/                Built skills, one self-contained folder each. Generated, do not edit
source/skills/         Skill sources. Edit these
source/shared/         Rules inserted into every skill (context.md)
source/config/         Pack file templates, schema, team rollout guide
source/assets/         Report shell (HTML), output schemas, reference notes
source/build.py        Builds skills/ from source/
docs/                  Documentation linked from the README, and README images (docs/images/)
evals/                 Headless end-to-end checks
```

`source/build.py` writes each `skills/<name>/SKILL.md` from `source/skills/<name>.md` with the shared rules inserted. It copies into each skill folder only the `config/` and `assets/` files that skill references, directly or through another file it carries. The build fails when a referenced file is missing or a `SKILL.md` passes 15 KB.

## Where to edit

| Change | Edit | Then |
|---|---|---|
| Skill behavior or report layout | `source/skills/<name>.md` | Run `python3 source/build.py` |
| Rules shared by all skills | `source/shared/context.md` | Run `python3 source/build.py` |
| Pack file templates | `source/config/*.md` | Run `python3 source/build.py` |
| Output schemas, report shell, reference notes | `source/assets/` | Run `python3 source/build.py` |

Never edit `skills/` by hand. Commit the rebuilt `skills/` folder with your source change.

## Rules for changes

1. **Keep each SKILL.md under 15 KB.** The build fails when a skill passes it.
2. **Version pack files.** Any edit to a file in `source/config/` raises its `version`, updates `updated`, and adds one Changelog line. See `source/config/SCHEMA.md` for the MAJOR, MINOR, and PATCH rules.
3. **Stay type-level.** Pack files never contain buyer names, buyer companies, exact amounts, or details of open deals.
4. **Name what each skill is not for.** The `description` in each skill's frontmatter says which skill to use instead. Keep that routing accurate when you add or rename a skill.
5. **Read-only by default.** A skill that writes to a CRM, inbox, or calendar asks for approval first.
6. **Add to CHANGELOG.md** for user-visible changes.

## Adding a skill

1. Create `source/skills/mia-<name>.md` with `name` and `description` frontmatter and a `{{SHARED}}` marker after the title.
2. If it produces a report, add its output schema as `source/assets/schemas/mia-<name>.md`.
3. Run `python3 source/build.py`.
4. Add a row to the skill table in `README.md`.
5. Bump the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

## Evals

`evals/run.sh` runs the skills headless on fictional CSV fixtures and checks the files they write (see `evals/README.md`). Run it after changing a skill source. It calls the model, so it costs a few dollars.

## README images

The images in `docs/images/` render from the HTML in `docs/images/src/` with the Mia night theme tokens. Edit the HTML, then run `docs/images/render.sh` (needs Google Chrome and Node; set `CHROME` to use another browser path). Images encode as mozjpeg at about 100 KB each. Commit the regenerated JPGs.

## License of contributions

By opening a pull request you agree to license your contribution under the AGPL-3.0-only terms in `LICENSE`.

## Reporting issues

Include the skill name, the data source you used (CRM, CSV, or a connector), the `Config:` line from the output, and what you expected.
