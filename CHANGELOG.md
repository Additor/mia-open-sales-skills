# Changelog

## 0.1.0-beta.2 (2026-10-20)

- License changed from Apache-2.0 to AGPL-3.0-only. `LICENSE`, `NOTICE`, both plugin manifests, the README, and the "Why this is free" text in `assets/readiness-line.md` now say so.
- README rewritten: install options, skill table with a "which skill, when" guide, safety defaults, pack file rules, team rollout, customizing, repository layout, and a plain-language license summary.
- Added `CONTRIBUTING.md` and `.gitignore`.

## 0.1.0-beta.1 (2026-10-19)

First public beta.

- Ten skills: pack setup, Daily Sync, Meeting prep, Call follow-up, Next move, Weekly Review, Forecast, At-risk review, CRM data check, Axes calibration.
- Pack files in `config/`, with versions, changelogs and a schema (`config/SCHEMA.md`).
- Team rollout guide in `config/TEAM-ROLLOUT.md`.
- Known limits: tested on exported CSV, calendar and call data; live connector paths and marketplace install are still being verified. Team files can drift between copies; the versions printed on every output are how to notice.
