# At-risk Review: DATA map

Fill the DATA object of `assets/report-shell.html` and change nothing else in the shell. Top-level keys: `meta`, `provisional`, `numbers`, `sections`, `howBuilt`, `config`. Sections always appear in the order below with the same ids; an empty one keeps its `empty` text. Item keys: `headline`, `meta`, `tags`, `detail`, `steps`, `evidence`, `sources`, `children`. Word limits are maxima. In DATA never write "you" or "your". Give the page every deal and let `cap` and `children` fold the rest. Spell each owner's name identically in every list.

## Top level

| Key | Content |
|---|---|
| meta.title | "<Name>'s At-risk Review" or "<Company> At-risk Review"; without a name, "At-risk Review" (personal) or "Sales Team At-risk Review" (team) |
| meta.skill | `mia-at-risk-review` |
| meta.view | View, with rep and open-deal counts in a team view, and each pipeline reviewed |
| meta.readCounts | "Activity read for the 40 largest among 112 open deals" when sampled |
| provisional | A line when any file used is a seed |
| numbers | Amount at risk (red deals); Amount gone quiet (says it overlaps with at risk); Unkept promises this month, shown as "N (M unconfirmed)". Leave out a tile that cannot be computed |
| howBuilt | What was read, "N of M" if sampled, where follow-ups were and were not checked, missing columns, any check skipped for a seed file, 60 words |
| config | Files used with versions |

The Habits `note` holds, in this order: the `measuredAgainst` line ("Measured against: the team's pack files" or "Measured against: CRM stages plus the default habits (no pack yet)"); any habit left out because the data cannot measure it (including an email-count habit with fewer than 10 logged outbound emails); and, in a team view, at most one standout statement. The statement describes the work only, what the habit looks like and counts on both sides ("recaps went out within a day for 9 of 10 demos with a booked next step, 2 of 8 without"). It ranks no one and passes no judgement on a named person.

## Sections

### habits: "Habits" (cap 0)
3 to 5 habits, as counts. Default `empty`: "No habit could be measured from the connected data."
- headline: the habit in the team's words
- meta: "done of total" ("4 of 13") and the source: Best deals, Recurring slips, Team standard, Inferred from wins, or Default habits
- detail: where the gap sits, 15 words
- children (team view): one item per rep with "done of total", shown only when a row is opened if there are more than 6 reps

```json
{ "headline": "Recap within a day of a demo", "meta": "4 of 13 · Recurring slips", "detail": "Missing mostly on demos that ran after 4 pm", "children": [{"headline": "Mireille", "meta": "3 of 5"}] }
```

### team-sweep: "Team sweep" (cap 0, team view only)
One line per rep. Default `empty`: "Not shown: no team view."
- headline: rep first name
- meta: open count and amount, amount and count at risk, gap count, unkept promises, weakest habit as "N of M". Gap count: each deal's distinct reasons (see scoring-axes `## Definitions`), summed per rep; counts only, no rank numbers, no scores
- children: that rep's at-risk deals

```json
{ "headline": "Tomas", "meta": "12 open · $310,000 · $64,000 at risk (3) · 7 gaps · 1 unkept promise · weakest: recap 1 of 6" }
```

### deals-at-risk: "Deals at risk" (cap 8 personal view, 6 team view)
Up to 40, most important first. Red status: a Risk signal is active. Default `empty`: "No active risk signal on the deals read."
- headline: company and reason, 12 words, a date or day count as evidence
- meta: owner (team view), amount, stage
- tags: 2 to 4 short tags, risk reason first (an active signal): quiet days, no next step, unkept promise, next-step date passed, who owes it, single-threaded
- detail: next action, 6 words
- steps: 2 to 4, verb first
- evidence: 2 to 4 lines, each a dated fact with its source
- sources

```json
{ "headline": "Harrow Tools: pricing promised Sep 29 never sent", "meta": "Mireille · $27,000 · Proposal", "tags": [{"text":"Unkept promise","tone":"warn"},{"text":"quiet 21 days","tone":"warn"}], "detail": "Next: send pricing today", "steps": ["Send Harrow Tools the pricing promised Sep 29", "Propose a 20-minute walkthrough this week", "Update the CRM close date after the reply"], "evidence": ["Call Sep 29: Mireille promised pricing by Oct 1", "Sent mail and shared inbox searched through Oct 19: nothing sent"], "sources": ["Call Sep 29", "Sent mail", "Shared inbox"] }
```

### this-week: "This week" (cap 5)
3 to 5 actions ranked by money and time sensitivity; at least one team habit in a team view. Default `empty`: "No action is open this week on the deals read."
- headline: action, verb first, names who to contact, 8 words
- meta: company (or "Team habit"), amount, owner (team view)
- detail: reason, 10 words
- steps: 2 to 4, verb first
- evidence: one line on why now

```json
{ "headline": "Send Harrow Tools the promised pricing", "meta": "Harrow Tools · $27,000 · Mireille", "detail": "Pricing promised Sep 29 is 18 days late", "steps": ["Attach the Oct quote to a reply to the buyer's procurement lead", "Offer two times for a walkthrough", "Note the send in the CRM"], "evidence": ["Promise logged on the Sep 29 call; no send found"] }
```

### whats-working: "What's working" (cap 0)
2 to 4 items: a habit kept, a deal that moved, a promise kept fast. Default `empty`: "No habit kept or promise met was found in the data read."
- headline: what, 8 words
- detail: note, 12 words

```json
{ "headline": "Demo recaps sent within a day after 5 of 6 demos", "detail": "Mireille's pipeline kept the habit through October" }
```

### off-process: "Off-process" (cap 8 personal view, 6 team view)
Every deal with gaps but no active risk signal, up to 40, most important first. Gold status. Default `empty`: "No deal with a gap and no active signal was found." The section `note` reads "Needs attention: gaps, no active risk signal". Close-out candidates are not listed here.
- headline: company and reason, 12 words
- meta: owner (team view), amount, stage
- tags: gap names (methodology, no Economic Buyer, Champion unknown, open request, close date out of step, stage ahead of the evidence, call not logged)
- detail: next action, 6 words
- sources

```json
{ "headline": "Quillon Marine: no decision process named at Negotiation", "meta": "Tomas · $19,000 · Negotiation", "tags": ["Methodology"], "detail": "Next: ask for approval steps", "sources": ["Calls and email, last 30 days"] }
```

### promises: "Promises" (cap 0)
Seller promises from the last 30 days that matter now, plus buyer requests still awaiting an answer (status "open request", promise "answer what the buyer asked"). Default `empty`: "No seller promise or open buyer request was found in the sources read."
- headline: company
- meta: owner, when (due or promised date)
- tags: status: missed, due, unconfirmed, kept or open request (a buyer request, not a promise)
- detail: the promise, 12 words; "(Name owes this)" when made on a colleague's deal
- evidence: where it was checked

```json
{ "headline": "Harrow Tools", "meta": "Mireille · due Oct 1", "tags": [{"text":"missed","tone":"warn"}], "detail": "Send pricing for the 40-seat plan", "evidence": ["Checked Mireille's sent mail, shared inbox and CRM through Oct 19; chat not connected"] }
```

### no-deal: "Buyer conversations with no deal" (cap 0)
Default `empty`: "No call with a buyer outside the open deals was found."
- headline: company
- detail: note, 15 words

```json
{ "headline": "Lindqvist Dairy", "detail": "Win-back call booked Oct 21; no open deal in the CRM" }
```

### close-out: "Close-out candidates" (cap 5)
Close-out candidates (scoring-axes `## Definitions`), largest amount first. A candidate that is also at risk keeps its row in Deals at risk, tagged "Overdue close date" where its close date has passed; one that is not at risk appears here only, not in Off-process. Default `empty`: "No deals are ready to close out."
- headline: company and the reason, 10 words
- meta: owner (team view), amount, stage, days without a two-way touch or days past the close date
- detail: suggested action, 8 words ("Close out unless a reply comes by Oct 28")
- sources

```json
{ "headline": "Ostrander Labs: no buyer reply in 74 days", "meta": "Mireille · $42,000 · Proposal · 74 days", "detail": "Close out unless a reply comes by Oct 28", "sources": ["Email search Oct 19", "CRM activity"] }
```

### on-track: "On track" (cap 0)
Count and names only. Default `empty`: "No deal was found free of gaps and signals."
- headline: "9 deals on track"
- detail: company names, comma separated

```json
{ "headline": "9 deals on track", "detail": "Brightmill Foods, Tallow Freight, Ostrander Labs" }
```
