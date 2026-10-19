# Report map: mia-crm-data-check

Fill `DATA` in `assets/report-shell.html` with the keys `meta`, `provisional`, `numbers`, `sections`, `howBuilt`, `whyFree`, `readiness`, `readinessUrl`, `config`. Section order is fixed. Every section is present on every run; use `empty` text when it has no items. No second-person wording anywhere in DATA except inside a quote. Deal names are company names without CRM suffixes. Amounts are numbers only; omit when unknown.

## Top-level keys

| Key | Content |
|---|---|
| meta.title | One sentence of at most 25 words for a sales leader: what the findings mean for the pipeline, for example how many deals lack what a forecast needs and which fields are missing most |
| meta.skill | `mia-crm-data-check` |
| meta.view | Rep, team (with rep count and open deal count), or company-wide |
| meta.readCounts | "N of M open deals checked" and the other reads |
| meta.firstRun | Per the shared rules: `true` when no earlier report of this skill exists. A run that builds the guide says "guide built this run" in `meta.view` |
| provisional | Provisional line when any file used is a seed (including a guide built this run) |
| numbers | Four tiles: Checked deals, Clean (passed every check), Need fixing, Fixes ready |
| howBuilt | At most 60 words on what was read, "N of M" sampling, and unread sources; note any limited check, any check skipped for a seed file or a missing column, and any read cap hit |
| whyFree, readiness, readinessUrl, config | Per the shared rules and `assets/readiness-line.md` |

## Sections

Item fields not listed for a section stay empty.

| id | title | cap | headline | meta | tags | detail | steps | evidence | children |
|---|---|---|---|---|---|---|---|---|---|
| categories | Categories | 0 (all seven, fixed order) | Category name and count, "29 of 41 pass" | Main reason or why not checked, at most 12 words | One status tag: OK (good), Needs attention (warn), or Not checked | Optional: one dated fact or the rule that moved the count, plus a relaxation suggestion | none | none | none |
| fixes | Fixes | 8 (6 in team view); the remainder is sorted by owner so the fold reads grouped | Deal and owner | The change in plain words a sales leader would use, at most 12 words | Name of the change group | Optional: why now | 2 to 3, always (approve in chat so the assistant applies it, or open the deal in the CRM and change it by hand) | Source, date, short quote; each at most 14 words | none |
| gaps | Deals with the most gaps | 8 (6 in team view) | Deal | Owner and stage | 2 to 4 issue tags of at most 4 words each | One sentence on the deal's state | 2 to 3 | Optional | none |
| team-sweep | Team sweep | 0; leader or both only; reps in alphabetical order, counts only, no ranking | Rep first name | Deal count and pass-count summary | none | Most common gap and its count, at most 12 words | none | none | Fixes, deals with gaps, and open decisions matched by owner; deals with no owner form their own row |
| decisions | Open decisions | 10 | Deal and owner | none | none | The question, at most 14 words | none (the item is a question for the owner) | none | none |
| duplicates | Duplicates | 10 | The two records | Rule: domain match, email match, or name match only | none | Which record to keep, at most 12 words | 2: open both records in the CRM, merge there (merging is never done by the assistant) | none | none |
| noticed | Also noticed | 3 | One line, at most 20 words | none | none | none | none | none | none |

Fixes are ordered by deal amount, largest first, then soonest close date. With no write tool, the fixes section `note` may point to the copy list (its own file, or a chat block). A category that was not checked, and a required closed-deal field whose column is absent, are named in the category line.

Default `empty` texts: categories "No category could be checked from the data read." · fixes "No fix is ready to apply." · gaps "No deal has gaps in the categories checked." · team-sweep "Not shown: no team view." · decisions "No decision is waiting on an owner." · duplicates "No duplicate records were found by the rules used." · noticed "Nothing else was noticed in the sources read."

Sources: every fix and gap item lists `sources` (the call, email, or CRM field behind each claim). Categories need none beyond the counts.

## Examples (invented)

categories:
```json
{ "headline": "Next steps · 29 of 41 pass", "meta": "Twelve deals have no meeting or dated task", "tags": [{"text": "Needs attention", "tone": "warn"}] }
```
fixes:
```json
{ "headline": "Harbor Quill · Dana", "meta": "Add Marcus Lee from the Oct 2 call as a contact", "tags": ["Fixes from calls and email"], "steps": ["Reply go ahead in chat to link the existing contact record.", "Or open Harbor Quill in the CRM and add Marcus Lee under contacts."], "evidence": ["Call Oct 2: named as the person signing the order"], "sources": ["Call Oct 2", "CRM contacts search"] }
```
gaps:
```json
{ "headline": "Tallow Freight", "meta": "Sam · Proposal", "tags": ["No close date", "No next step", "One contact"], "detail": "Proposal stage, but no proposal was sent and nothing is booked.", "steps": ["Ask Sam whether a proposal is planned and set a close date.", "Book a buyer meeting or add a dated task by Friday."], "sources": ["CRM record", "Email search"] }
```
team-sweep:
```json
{ "headline": "Priya", "meta": "14 deals · 41 of 56 checks pass", "detail": "Close dates missing on 6 deals", "children": [{ "headline": "Lumen Orchard · Priya", "meta": "Set close date to Nov 30", "steps": ["Approve in chat.", "Or set it in the CRM."] }] }
```
decisions:
```json
{ "headline": "Brightwell Mills · Jo", "detail": "Deal sits in Negotiation without buyer replies. Move back to Proposal?" }
```
duplicates:
```json
{ "headline": "Kestrel Ridge Inc / Kestrel Ridge", "meta": "Domain match", "detail": "Keep Kestrel Ridge Inc; it holds both deals.", "steps": ["Open both records in the CRM.", "Merge them there, keeping the one with the deals."] }
```
noticed:
```json
{ "headline": "Two calls this month with Oakfield Print, which has no deal in the CRM." }
```
