# Report map: mia-axes-calibration

Fill `DATA` in `assets/report-shell.html` with the keys `meta`, `provisional`, `numbers`, `sections`, `howBuilt`, `config`. Section order is fixed and every section appears on every run. No second-person wording in DATA except inside a quote. The report describes deals and criteria, never people. Deal names are company names without CRM suffixes.

## Top-level keys

| Key | Content |
|---|---|
| meta.title | One sentence of at most 25 words stating the main finding, for example where the criteria and outcomes diverged most |
| meta.skill | `mia-axes-calibration` |
| meta.view | Rep, team (with rep count), or company-wide |
| meta.readCounts | "N of M closed deals read" |
| provisional | Provisional line when scoring-axes is a seed; call its categories "starting values" |
| numbers | Closed deals analyzed, Won, Lost, From snapshots, Reconstructed |
| howBuilt | At most 60 words: what was read, the 30-day cutoff (or that it was not enforced in a lifetime replay), which deals used snapshots and which were reconstructed, unread sources, any check skipped for a seed file. Untestable signals go in `limits`, not here |
| config | Per the shared rules; `config` names the scoring-axes version used |

## Sections

| id | title | cap | headline | meta | tags | detail | steps | evidence | children |
|---|---|---|---|---|---|---|---|---|---|
| replay | Replay summary | 0 (one item per category: Commit, Best Case, Pipeline, then Deal at risk flag) | Category and result, "Commit: 9 won, 3 lost" | Number of deals placed there, at most 12 words | Optional tag for a notable result | One sentence, at most 25 words | none | none | none |
| disagreements | Where the criteria disagreed with outcomes | 0 (two items: classed Commit but lost; outside Commit and Best Case but won) | Group name and deal count | Facts the deals share, at most 20 words | none | What the shared facts suggest about the criteria, at most 30 words | none | One dated fact per deal, at most 14 words each | One child per deal: headline deal, meta close date and outcome, detail what was true at 30 days out |
| signals | Signals | 0 (one item per Risk signal) | Signal name | Active before N of M lost deals and N of M won deals ("Not tested: <what is missing>" when Not testable) | One of: separates (good), does not separate (warn), never active, Not testable | Effect of moving the threshold, with before and after classification counts, at most 30 words | none | none | none |
| edits | Proposed edits | 0 | Setting with change, "Deal quiet: N = 14 to N = 21" | "Backed by N deals" (deals where the edited signal fires), at most 12 words | Version bump needed (MAJOR, MINOR, or PATCH; below 1.0.0 a classification-changing edit is MINOR); "weak" in warn tone when fewer than 8 deals back it | Why, at most 30 words | 2 to 3: review the edit, save the updated scoring-axes.md, add a Changelog line and raise the version | The supporting deals, one line each, at most 14 words | none |
| limits | What this run cannot conclude | 0 | One limit per item, at most 25 words | none | none | none | none | none | none |

Lifetime replay (see the skill): when closed-deal data holds only lifetime summaries, the replay headlines read "Commit on testable gates: 9 won, 3 lost", every count in replay, signals and edits carries "per CRM, lifetime" in `meta`, and each signal the data cannot test is a signals item tagged "Not testable" (plain tone) with `meta` naming what is missing, and is also named in limits. A competitor name with no date or preference is not testable for Competitor mention.

Default `empty` texts: replay "No closed deal could be placed in a category." · disagreements "No closed deal contradicted its category." · signals "No Risk signal could be tested on the closed deals." · edits "The replay supports no change to the criteria." · limits "No limit beyond the sample size was found."

Every item in `disagreements` and `edits` lists `sources` (the calls, emails, or CRM fields behind it). If the sample gate fails, no report is built; the chat reply states how many more closed deals are needed.

## Examples (invented)

replay:
```json
{ "headline": "Commit: 9 won, 3 lost", "meta": "12 deals placed in Commit", "detail": "Three Commit losses all lacked a booked next step by day 30 before close." }
```
disagreements:
```json
{ "headline": "Classed Commit, lost: 3 deals", "meta": "All had one buyer contact", "detail": "Single threading may deserve to be a Commit gate.", "evidence": ["Mossgate Labs: only one buyer replied in the 30 days before close"], "sources": ["Email, Sep 4", "Call, Aug 29"], "children": [{ "headline": "Mossgate Labs", "meta": "Lost, Sep 30", "detail": "Economic Buyer had joined a call, but no other contact replied." }] }
```
signals:
```json
{ "headline": "Deal quiet", "meta": "Active before 7 of 11 lost deals and 6 of 14 won deals", "tags": [{"text": "does not separate", "tone": "warn"}], "detail": "At 21 days it fires on 4 lost and 1 won; classification changes on 5 deals." }
```
edits:
```json
{ "headline": "Deal quiet: N = 14 to N = 21", "meta": "Backed by 9 deals", "tags": ["MAJOR"], "detail": "A 14-day window flagged as many won deals as lost ones.", "steps": ["Review the edit against the replay.", "Save the updated scoring-axes.md in the project.", "Add a Changelog line and raise the version."], "evidence": ["Pinebrook Co: won after a 16-day silence"], "sources": ["Email, Jul 11"] }
```
limits:
```json
{ "headline": "Evidence for 6 deals was rebuilt from activity, since no stage history exists." }
```
