# Guide

Team rollout, customizing the pack files, and what the skills read and write.

## Team rollout

1. The leader runs `mia-pack-setup`, reads the six team files, fixes them, and sets `status: reviewed`.
2. The leader shares them as one `team-pack` folder, or commits them under `mia-pack/` in a shared repository, and posts the current version of each file.
3. Each rep adds the files to `mia-pack/` and runs `mia-pack-setup`, which builds only their voice and working style.
4. A rep who disagrees with a criterion sends the leader the file, the reason and the deals affected. Team files are never edited locally.

Every output ends with a `Config:` line. Compare those numbers across the team to confirm everyone runs the same files. Full procedure: [source/config/TEAM-ROLLOUT.md](../source/config/TEAM-ROLLOUT.md).

## Customize

Edit the pack files that setup created in `mia-pack/`:

| To change | Edit |
|---|---|
| Thresholds, categories, risk signals | `mia-pack/scoring-axes.md` |
| Stages and entry conditions | `mia-pack/deal-lifecycle.md` |
| Team rules and weekly review items | `mia-pack/team-standards.md` |
| How drafts sound | `mia-pack/voice.md` |

Raise the file version and add a Changelog line with each edit. The `source/config/` folder in this repository holds the templates those files start from. File list, frontmatter, versioning and precedence: [pack-files.md](pack-files.md).

To change what a skill itself does or how a report is laid out, edit `source/skills/<name>.md` in a fork and run `python3 source/build.py`. The build regenerates `skills/`, so never edit that folder by hand.

## Safety and privacy

- Report skills are read-only toward your tools. They never send, post or write to your CRM, and in a coding agent they write only to `mia-pack/` and `mia-reports/`.
- Skills that propose changes (`mia-call-follow-up`, `mia-crm-data-check`) wait for your explicit approval.
- Skills run when you call them and read only the sources you connect.
- Reports make no network request when they open and contain no tracking links.
- Reports describe work, not people: no scores, rankings or personal adjectives for reps.
