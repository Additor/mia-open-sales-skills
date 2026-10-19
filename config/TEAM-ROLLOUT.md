# Team rollout

How a team shares one set of pack files and keeps them in step.

## For the leader

Run mia-pack-setup on your own data. It writes the six team files: deal-lifecycle, buyers-and-competition, market-physics, winning-plays, team-standards and scoring-axes. Read each one and fix what is wrong, because the reps will inherit every threshold and definition you leave in. When a file reads true, set `status: reviewed` and raise its version.

Then save the team pack bundle: those six files plus this page, in one folder named team-pack (or a zip). Share it with each rep through whatever your team already uses, whether chat, email or a shared drive, as that single folder or zip, never as loose files. Finish with one message that tells reps the current version of each file, so everyone has a number to compare against.

## For each rep

Put the team files in the same place as your own pack files, and do not edit them. Then run mia-pack-setup. It sees the team files and builds only your voice and your working style from your own deals and email.

Until the leader has marked the team files reviewed, your first results carry a provisional label. That is expected, and it goes away once the files change from seed to reviewed.

At the end of every output you will find a `Config:` line listing the files used and their versions. Compare it with the versions the leader announced. If a number differs, ask for the latest bundle before you trust the result.

## When team files change

The owner of the file edits it, raises the version, adds a Changelog line, re-shares the whole bundle and announces the new versions. Sharing the whole bundle, not one file, keeps copies from drifting apart.

A rep who thinks a criterion is wrong does not edit it locally. Send the leader the file name, the reason, and the kind of deals it affects. A suggestion from calibration travels the same way: the rep passes it to the owner, and the owner decides.

## What can differ per person

Only voice.md, working-style.md and personal plays. Thresholds, definitions, stages and team rules never differ. If a rep's habit departs from the team process, it belongs in their working style, not in a changed team file.

## Limits

The free pack cannot force everyone onto the same files. Each person holds their own copies, and copies can drift: someone misses a message, keeps an older folder, or tweaks a number to get a result they prefer. The versions printed on every output are how you notice, and noticing depends on people actually checking them. A single shared source with central updates is what a hosted setup provides; Mia is one such option, for teams that outgrow the manual routine.
