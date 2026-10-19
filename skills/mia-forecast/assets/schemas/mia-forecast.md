# Forecast: DATA map

Fill the DATA object of `assets/report-shell.html` and change nothing else in the shell. Top-level keys: `meta`, `provisional`, `numbers`, `sections`, `howBuilt`, `whyFree`, `readiness`, `readinessUrl`, `config`. Sections always appear in the order below with the same ids; an empty one keeps its `empty` text. Item keys: `headline`, `meta`, `tags`, `detail`, `steps`, `evidence`, `sources`, `children`. Word limits are maxima. In DATA never write "you" or "your". The forecast makes no probabilities and no scores.

## Top level

| Key | Content |
|---|---|
| meta.title | Team view "<Company> Forecast", fallback "Team Forecast"; personal view "<user first name>'s Forecast", fallback "Forecast" |
| meta.skill | `mia-forecast` |
| meta.view | View and period as the user named it (a month, two months, a quarter or a date range; the current quarter when none): "Team view · Q4 · 6 reps" |
| meta.readCounts | "Classified 120 of about 180 deals in the period" when sampled |
| provisional | A line when scoring-axes or any file used is a seed; categories are then called starting values |
| numbers | Tiles: Deals in period; CRM commit (field name in the label, the `crmLabel`: "CRM commit (Forecast category)"); Evidence commit; Slip. With a target, add Target and Coverage ratio. One more tile gives the spread: "3 Commit · 7 Best Case · 12 Pipeline". Amounts are sums of deals with amounts; with no amounts, tiles show counts |
| howBuilt | What was read, CRM field used for CRM commit, "N of M" if sampled, unread sources, deals with no amount (count), any check skipped for a seed file, 60 words |
| whyFree, readiness, readinessUrl | From `assets/readiness-line.md` |
| config | Files used with versions |

The one line explaining the two values goes in the `note` of the Differences section, which sits directly under the tiles: CRM commit is what the CRM holds today; Evidence commit is what the buyer's own words and actions support.

The Move and Close-out lists appear in the chat reply only, not in DATA. A deal in both appears only in Close-out, and a Close-out candidate (scoring-axes `## Definitions`) appears in Close-out whatever the period, though it enters Deals only when its CRM close date falls in the period. In Deals it carries the "Overdue close date" tag, not Slip, has no category label and sits last, and no category sum, spread tile or Differences row counts it.

Evidence date display: when the buyer gave a date, date fields show the Evidence date; when not, they show "not stated" and the computed estimate goes in `detail` labelled "estimated" (classification reference, section 3).

## Sections

### differences: "Differences" (cap = number of items shown)
One section, two groups in this order: up to 6 deals where the CRM is ahead of the evidence (8 in team view, largest amount first), then up to 6 where the evidence is ahead of the CRM (including deals dated within 30 days after the period only when evidence supports an earlier close, inside the period). Set `cap` to the number of items listed. Empty with fewer than 5 deals in the period, or when no CRM category exists anywhere. Default `empty`: "Fewer than 5 deals in the period, or no CRM category to compare, so differences were not checked."
- headline: company and the shift, "CRM Commit to Evidence Best Case"
- meta: owner, amount, "CRM date to Evidence date" ("not stated" when the buyer gave no date)
- tags: "CRM ahead" or "Evidence ahead"; "Slip" if flagged
- detail: one fact about the buyer
- sources

```json
{ "headline": "Quillon Marine: CRM Commit to Evidence Best Case", "meta": "Tomas · $19,000 · Oct 30 to Dec 4", "tags": [{"text":"CRM ahead","tone":"warn"},{"text":"Slip","tone":"warn"}], "detail": "Buyer's finance lead said board approval is Dec 3 (email Oct 9)", "sources": ["Email Oct 9"] }
```

### deals: "Deals" (cap 0)
Every in-period deal up to 120, most certain first, ties by earlier Evidence date. Default `empty`: "No open deal has a CRM close date in the period." Each row is at most four short lines.
- headline: company and why, why is 10 words, one fact behind the label
- meta: owner, stage, amount ("no amount" when unknown), CRM date to Evidence date ("not stated" when the buyer gave no date)
- tags: label (the category: Commit, Best Case or Pipeline; none for an overdue-close-date deal), "CRM: <category>", "Evidence: <category>", Deal at risk (warn), Slip (warn), "Overdue close date" (warn) when the CRM date has passed
- detail: "Open gate: <blocker, 8 words>. Move: <12 words, starts with a name>"; "Estimated finish <date>" when the buyer gave no date. Commit with nothing missing: the buyer's date as the expected signing date
- steps: 2 to 4 verb-first steps for the move; for no available move, one step saying what to wait for or "Close out"
- evidence: 2 to 5 lines with date and source, buyer side first. The first line is "Buyer date: <date, who, title, source>" or "Buyer date: none given". Then gates met, signals active, buyer titles and quotes (exact words only; else "Logged: <paraphrase>"), "Economic Buyer not named on any call or email" when true, "note only, unconfirmed" when a seller note is the only source
- sources

```json
{ "headline": "Brightmill Foods: order form with buyer legal since Oct 14", "meta": "Tomas · Contracting · $18,500 · Oct 30 to Oct 30", "tags": ["Commit", "CRM: Commit", "Evidence: Commit"], "detail": "Open gate: signature due Oct 28. Move: Tomas: confirm legal's review date with Ines Calloway on Oct 21", "steps": ["Email Ines Calloway on Oct 21 asking for legal's review date", "Offer a 15-minute call if a clause is open", "Log her answer in the CRM"], "evidence": ["Buyer date: Oct 28, Ines Calloway (Controller), email Oct 14", "Gates met: Economic Buyer on call Oct 8; decision date stated; next step booked", "No risk signal active"], "sources": ["Call Oct 8", "Email Oct 14"] }
```

### likely-to-slip: "Likely to slip" (cap 0)
Deals with Slip (buyer-named date or Evidence date after the period), largest amount first. They also appear in Deals. Default `empty`: "No deal has a buyer-named or estimated date after the period."
- headline: company and Evidence date ("estimated <date>" when the buyer gave none)
- meta: owner, amount, CRM date
- detail: blocker, 8 words
- sources

```json
{ "headline": "Quillon Marine: Evidence date Dec 4", "meta": "Tomas · $19,000 · CRM date Oct 30", "detail": "Board approval named for Dec 3", "sources": ["Email Oct 9"] }
```

### team-sweep: "Team sweep" (cap 0, team view only)
One row per rep, largest gap between CRM commit and Evidence commit first. Empty with fewer than 5 deals in the period. Default `empty`: "Fewer than 5 deals in the period, so the team sweep was not built."
- headline: rep first name, spelled the same everywhere
- meta: CRM commit amount and Evidence commit amount
- detail: Coach's question, 20 words, naming one deal and the decision needed, no ranking or personal adjective
- children: that owner's deals as Deals-style items

```json
{ "headline": "Tomas", "meta": "CRM commit $64,000 · Evidence commit $18,500", "detail": "Coach's question: Quillon Marine has no meeting booked; keep an Oct 30 close date or move it to December?", "children": [{"headline": "Quillon Marine: board approval Dec 3", "meta": "$19,000 · CRM Commit · Evidence Best Case"}] }
```

### how-it-works: "How the forecast works" (cap 0)
Plain-language items, one per rule (default `empty`: "The rules could not be read from scoring-axes."), so anyone can check a label: the three categories and their gates, the two flags, how the Evidence date is set, and what counts as evidence. The last item carries the snapshot.
- headline: the rule's name ("Commit", "Slip", "Snapshot")
- detail: the rule in plain words, taken from scoring-axes
- evidence (snapshot item only): one compact machine-readable line of deal identifiers, categories, dates and config versions, with a note that nothing has been saved anywhere

```json
{ "headline": "Snapshot", "detail": "Optional line to keep for mia-axes-calibration; nothing has been saved.", "evidence": ["{\"period\":\"Q4\",\"config\":{\"scoring-axes\":\"0.1.1\"},\"deals\":[{\"id\":\"d-104\",\"crm\":\"Commit\",\"evidence\":\"Best Case\",\"date\":\"2026-12-04\"}]}"] }
```
