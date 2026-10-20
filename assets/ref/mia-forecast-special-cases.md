# Forecast: special cases

Read this when data is missing, when the user asks about a single deal, or when closing the report.

## Missing data
No CRM: read an attached or pasted CSV as the CRM (see `assets/ref/shared-csv-as-crm.md`); without one, ask once for a CSV (owner, stage, amount, close date, forecast category). With none, take deals from buyer conversations that carry a date or decision, leave CRM values empty and mark the page as built without a CRM. If no CRM classification exists anywhere (no forecast field, no stage mapping), show only Evidence values, leave CRM category empty, empty Differences, and say so in `howBuilt`. No call recordings: classify from email, calendar and CRM activity, and note in `howBuilt` that gates needing the buyer's words were judged from email alone. Under 5 deals in the period, empty Differences and Team sweep.

## One-deal question
When the user asks about one deal ("Is Brightwell really Commit?"), skip the report and answer in chat: CRM category, Evidence category and date, gates passed, signals active, what the buyer has not yet done, the evidence lines. Close by offering the full forecast.

## Snapshot
The last item of "How the forecast works" carries, in `evidence`, one compact machine-readable line (deal identifiers, categories, dates, config versions, no buyer names) for mia-axes-calibration. In workspace mode, append that line to `mia-reports/snapshots.jsonl` (one JSON object per line) and say so. In chat mode, say the line is shown for the user to keep and was not saved.
