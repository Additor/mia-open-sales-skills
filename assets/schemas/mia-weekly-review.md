# Weekly Review: DATA map

Fill the DATA object of `assets/report-shell.html` and change nothing else in the shell. Top-level keys: `meta`, `provisional`, `numbers`, `sections`, `howBuilt`, `config`. Sections always appear in the order below, with the same ids every run; an empty section keeps its `empty` text (defaults below). Item keys: `headline`, `meta`, `tags`, `detail`, `steps`, `evidence`, `sources`, `children`. Word limits are maxima. In DATA never write "you" or "your".

## Top level

| Key | Content |
|---|---|
| meta.title | Rep view: "<Name>'s Weekly Review". Team view: "<Company> Weekly Review". Without a name: "Weekly Review" (rep) or "Sales Team Weekly Review" (team) |
| meta.skill | `mia-weekly-review` |
| meta.view | View and cadence, with rep and open-deal counts in a team view, and both windows with dates: "Team view · 6 reps · 84 open deals · weekly · moved and closed Oct 12 to Oct 19 · closing Oct 19 to Oct 26" |
| meta.readCounts | "Read 100 of about 340 open deals" (only the numbers that apply) |
| meta.generatedAt, meta.firstRun | Timestamp; true on a first run |
| provisional | One line when any file used is a seed, else "" |
| numbers | Tiles: Open deals (count and amount in the value), At risk (amount and count), Closing this period (count and amount of close dates from today through today+7), Moved forward (count). Team view uses team figures |
| howBuilt | What was read, "N of M" if sampled, unread sources, any check skipped for a seed file, 60 words |
| config | Files used with versions, for example "scoring-axes 0.1.1, deal-lifecycle 0.1.0" |

## Sections

### next-week: "Next week" (cap 5)
Top 3 to 5 actions, ranked by time sensitivity. Default `empty`: "No action is open for next week on the deals read."
- headline: action, verb first, names who to contact, 8 words
- meta: company, amount, owner (team view only)
- tags: the main active signal, if any
- detail: reason, 10 words
- steps: 2 to 4, verb first
- evidence: a single line explaining the timing, with its date and source
- sources: calls, emails or CRM fields behind it

```json
{ "headline": "Send Ostrander Labs the promised security summary", "meta": "Ostrander Labs · $42,000 · Mireille", "tags": [{"text":"Our overdue commitment","tone":"warn"}], "detail": "Security summary promised Oct 6 has not gone out", "steps": ["Attach the SOC summary to a reply to Priya Raman today", "Ask for a date to review it with her IT lead", "Log the send in the CRM deal notes"], "evidence": ["Call Oct 6: Mireille promised the summary by Oct 9; no sent mail since"], "sources": ["Call Oct 6", "Sent mail search Oct 17"] }
```

### moved-forward: "Moved forward" (cap 0)
Default `empty`: "No stage advance, win or decision-maker meeting was found in the look-back window."
- headline: company and the single event, 8 words
- meta: owner, amount
- tags: event type ("Stage advanced", "Won", "Pilot started", "Decision-maker meeting")
- detail: date and fact; if the deal is also at risk, say so
- sources: CRM stage history, calendar or call

```json
{ "headline": "Brightmill Foods: pilot started Oct 13", "meta": "Tomas · $18,500", "tags": [{"text":"Pilot started","tone":"good"}], "detail": "Pilot kicked off Oct 13; no Economic Buyer named yet", "sources": ["Calendar Oct 13", "CRM stage history"] }
```

### closed: "Closed" (cap 0)
Wins and losses at equal weight, closed in the look-back window. Default `empty`: "No deal closed in the look-back window." The empty text may name deals that fell outside the window ("Tallow Freight closed Oct 10, 9 days ago").
- headline: company and result
- meta: owner, amount
- tags: "Won" (good) or "Lost" (warn)
- detail: win, what carried it over, 8 words; loss, CRM loss reason 8 words, else "No reason logged"

```json
{ "headline": "Tallow Freight: lost", "meta": "Mireille · $27,000", "tags": [{"text":"Lost","tone":"warn"}], "detail": "Lost to incumbent on price", "sources": ["CRM loss reason"] }
```

### where-deals-sit: "Where deals sit" (cap 0)
One item per stage in stage order. Empty when fewer than 5 open deals in the view's scope. Default `empty`: "Fewer than 5 open deals in scope, so the stage view was not built."
- headline: stage name as the pack spells it
- meta: count, amount, amount at risk
- detail: how many deals lack what the stage requires, 8 words

```json
{ "headline": "Proposal", "meta": "9 deals · $212,000 · $64,000 at risk", "detail": "4 of 9 lack a second buyer contact" }
```

### at-risk: "At risk" (cap 8 personal view, 6 team view)
Every at-risk deal up to 40, time urgency first (the soonest date that matters on the deal: close date, a promise or step due), then larger amount; the items past the cap are grouped by owner. Default `empty`: "No active risk signal on the deals read."
- headline: company and reason, reason 8 words with the active signal first
- meta: owner (team view), amount, stage, quiet days and last touch channel ("quiet 18 days, email"); "no contact recorded" when none
- tags: active signal names with tone warn; other flags (past close date, long in stage, stage out of step, recurring slip) as plain tags
- detail: next action, 6 words
- steps: 2 to 4, verb first
- evidence: 2 to 4 lines, each a dated fact with its source
- sources

```json
{ "headline": "Ostrander Labs: no next step, quiet 18 days", "meta": "Mireille · $42,000 · Proposal · quiet 18 days, email", "tags": [{"text":"No next step","tone":"warn"},{"text":"Deal quiet","tone":"warn"}], "detail": "Next: book review with IT lead", "steps": ["Email Priya Raman a Nov 4 review slot", "Copy the IT lead named on Oct 6", "Set a dated CRM task for Oct 24"], "evidence": ["Last buyer reply Oct 1 (email)", "No meeting on calendar through Nov 2"], "sources": ["Email search Oct 19", "Calendar"] }
```

### closing: "Closing" (cap 0)
Open deals with a close date in the forward window (today through today+7 weekly). Skip when no deal has a close date and flag the count without one. Default `empty`: "No open deal has a close date in the forward window."
- headline: company
- meta: owner (team view), amount, close date
- tags: "on track" (good) or "at risk" (warn), never anything in between
- detail: note, 8 words

```json
{ "headline": "Brightmill Foods", "meta": "Tomas · $18,500 · Oct 30", "tags": [{"text":"on track","tone":"good"}], "detail": "Order form with buyer legal since Oct 14" }
```

### close-out: "Close-out candidates" (cap 0)
One summary item for the Close-out candidates (scoring-axes `## Definitions`): open deals past their close date or silent past the Definitions limit. A deal that is also at risk appears here and in At risk. Default `empty`: "No open deal is past its close date or long silent."
- headline: count and total
- detail: names with days past or days silent
- children: one item per deal (headline company, meta owner, amount, days past or silent, tags "Overdue close date" where it applies, detail: suggested new date or close-out)

```json
{ "headline": "2 candidates · $31,000", "detail": "Quillon Marine (12 days past close), Ostrander Labs (74 days silent)", "children": [{"headline": "Quillon Marine", "meta": "Tomas · $19,000 · 12 days past Oct 7", "tags": ["Overdue close date"], "detail": "Propose Nov 15 or close out"}] }
```

### team-sweep: "Team sweep" (cap 0, team view only)
One row per rep who owns open deals, largest amount at risk first; a leader with no deals gets no row. Default `empty`: "Not shown: no team view."
- headline: rep first name, spelled the same in every list
- meta: open count and amount, amount and count at risk, closing this period
- tags: optional, from `## What leaders review each week`
- detail: Coach's question, 15 words, naming one deal and one decision, backed by evidence; no ranking, score or adjective about the person
- evidence: 2 to 4 dated facts behind the question
- children: that owner's At risk and Moved forward items

```json
{ "headline": "Tomas", "meta": "12 open · $310,000 · $64,000 at risk (3) · 2 closing", "detail": "Coach's question: should Quillon Marine keep Nov 15, with no meeting booked?", "evidence": ["Quillon Marine: last buyer reply Sep 24 (email)", "No dated step in CRM"], "children": [{"headline": "Quillon Marine: no next step", "meta": "$19,000 · Proposal"}] }
```
