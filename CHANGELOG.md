# Changelog

## 0.2.0 (2026-10-20)

- Two modes. In a coding agent (Claude Code, Codex and others) `mia-pack-setup` and `mia-crm-data-check` write pack files to `mia-pack/` after you confirm, and report skills save to `mia-reports/`. Chat apps keep the download and copy-block flow. Skills read `mia-pack/` first, then attached files, then the `config/` templates.
- `mia-axes-calibration` no longer stops at a bare refusal below 20 closed deals: 8 to 19 run a directional replay with no proposed edits, and fewer than 8 say what data to bring. Forecast snapshots are saved to `mia-reports/snapshots.jsonl` in workspace mode and read from there.
- `mia-call-follow-up` saves its document as Markdown instead of offering a report with no layout. `mia-daily-sync` is described as a one-screen page.
- `mia-pack-setup` no longer writes company names or exact amounts into pack files, for won and lost deals as well as open ones. Found by the new evals.
- Added `evals/`: five headless end-to-end cases with fictional fixtures (`evals/run.sh`).
- README images use the official Mia logo; the hero puts it at the bottom right. Removed captions, footers and wording that read as unfinished.
- Sources moved into `source/` (skills, shared rules, config templates, assets, `build.py`). Each skill folder now carries only the files it references, so `skills/` dropped from 178 to 132 files. The build fails on a missing reference or a `SKILL.md` over 15 KB.
- README cut to a hook, a report preview and a three-step quick start. Team rollout, Customize and Safety and privacy moved to `docs/guide.md`.
- Install with `npx skills add Additor/mia-open-sales-skills`, plus Codex paths. New `docs/environments.md`.

## 0.1.0 (2026-10-20)

First public release.

- Ten skills: pack setup, Daily Sync, Meeting prep, Call follow-up, Next move, Weekly Review, Forecast, At-risk review, CRM data check, Axes calibration.
- Pack files in `config/`, with versions, changelogs and a schema (`config/SCHEMA.md`, `docs/pack-files.md`).
- Team rollout guide in `config/TEAM-ROLLOUT.md`.
- License: AGPL-3.0-only (`LICENSE`, `NOTICE`, both plugin manifests).
- Report footers hold the "How this was built" note and the `Config:` line. Reports contain no tracking links.
- README with quick start, install options, skill list and images (`docs/images/`, rendered from `docs/images/src/` in the Mia night theme). `CONTRIBUTING.md` documents the layout and build.
