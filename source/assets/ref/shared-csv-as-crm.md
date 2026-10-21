# CSV as CRM

Read this when a CSV or pasted table stands in for a CRM. If one is already attached or pasted in this conversation, read it and do not ask for another.

## No CRM at all
Use an attached or pasted CSV without asking for one. With none, ask once for a CSV (owner, stage, amount, close date, next step, last activity). Failing that, build a light version from email, calls and calendar, labelled as built without a CRM, with no stage or amount totals. A skill's read caps apply to records; with CSV files read the whole file.

## Mapping columns
Match columns by meaning, not exact header. Look for: owner, stage, amount, close date, created date, stage-entered date, next step and its due date, commit call (the rep's forecast category), competitor, champion, Economic Buyer engaged, and pushes (times the close date moved; usually a lifetime count, so apply the Period rule in scoring-axes `## Definitions`). A missing column means the checks that need it are skipped; name them in `howBuilt`.

Last activity is the latest two-way touch (see scoring-axes Definitions): use the field when one exists; otherwise the latest dated two-way row for the deal in an activity table. Two-way: a row where the buyer replied or attended, or the buyer wrote to the user.

## Stage timing
When a typical-days-per-stage file is supplied, use it for Stalled stage in place of the table in deal-lifecycle.

## Quotes and logged summaries
Activity logs hold summaries, not the words as spoken or written. When a deal has only logged summaries, write "Logged: <paraphrase>, <date>" (for example "Logged: buyer asked for pricing, Oct 3") with no quotation marks, and never present it as a quote or an exact phrase. A section that asks for quotes and has a minimum item count may show fewer items when the evidence does not exist: state the count it has; with none, follow the schema (its empty text, or omit the section). A section that is omitted when no exact phrases exist (Meeting prep, Buyer's words) is omitted.

## No calendar
With no calendar, or for a deal the calendar does not cover, a dated CRM next step stands in under valid next step in scoring-axes `## Definitions`. Label every verdict that rests on it "per CRM".

## A source that was never connected
Say so in one line in `howBuilt` (inside its 60 words) and again in the sources line, naming the source and the checks skipped, in this form: "<Source> not connected, so <checks> were skipped." For example: "Calendar not connected, so booked-meeting checks were skipped and dated CRM next steps count per CRM." For several unconnected sources, one combined sentence is allowed: "Calendar, email and calls not connected, so those checks were skipped."
