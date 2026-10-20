# Report rules

Read this at the start of any skill that builds a report.

## Sections
Build the report without asking, with the same sections in the same order every run, except where a schema names a reorder or omits empty sections (Meeting prep). An empty section keeps its id and a one-line `empty` reason saying what was not checked or found; schemas give defaults. Under 5 open deals in the view's scope, empty the affected sections with the reason.

## Title
With no name available, the title is "Sales Team <Skill name>" for a team view and "<Skill name>" for a personal view (Forecast keeps "Team Forecast").

## First run
Look for a previous report of the same skill in the project folder or conversation. None means a first run: set `firstRun`, say "first run", skip comparisons. Compare with that report only; there is no other storage.

## DATA
DATA never says "you" or "your": use first names or "the team". Quotes and the fixed Meeting prep title "Since your last call" are the only exceptions. Amounts are numbers. An unknown value stays empty (n/a for tiles); a known zero shows 0.

## howBuilt
At most 60 words. It names the sources read, "N of M" when sampled, the sources not read, and any check skipped because a seed file lacks what it needs (one clause).

## Format and footer
Fall back from artifact to HTML to Markdown. The footer holds one collapsed note, "How this was built", and the `Config:` line.
