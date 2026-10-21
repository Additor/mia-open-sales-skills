# Daily Sync: DATA section map

Fill the DATA object in assets/report-shell.html and change nothing else in the shell. Use the same seven sections on every run, including scheduled runs, in the fixed order below. Never drop or add a section: one with no content keeps its id and its place, leaves `items` empty and sets `empty` to one line saying what was not checked or found. The order changes only in the two cases under Order rules. Never write "you" or "your" in DATA; use first names for people and "the team" for the team. Quotes are the one exception. Name a deal by its company, with any CRM suffix removed. Put an amount in only when the CRM holds one and leave it out when unknown; a known zero shows 0.

## Top-level keys

| Key | Content |
|---|---|
| meta | `title` "Daily Sync", `skill` "mia-daily-sync", `generatedAt`, `view` (rep or leader, plus rep count and open-deal count for a team view, and the working day if built for the next one), `firstRun`, `readCounts` (for example "112 of 112 open deals, 6 meetings") |
| provisional | The seed line when any file used has `status: seed`; otherwise empty |
| numbers | Three tiles: Meetings today, Replies waiting, Deals at risk (all flagged deals, not only those shown). A tile whose value is unknown shows "n/a" and its label says why, for example "Meetings today (no calendar)" |
| sections | The seven below, in this order |
| howBuilt | Sources read, "N of M" if sampled, sources that could not be read, any check skipped for a seed file (60 words or fewer) |
| config | Files used with versions, for example "working-style 0.1.0, scoring-axes 0.1.1" |

Leave `meta.view` showing what was built so the user can ask for another view. `meta.title` is "Daily Sync".

## Sections

| id | title | cap | Order note |
|---|---|---|---|
| next | Next moves | 5 | First, always. |
| since | Since yesterday | 6 | Second. |
| meetings | Today's meetings | 0 (all sales calls) | Third |
| replies | Replies waiting | 5 | |
| risks | Risks | 3 per rep | Fifth |
| team | Team sweep | all reps | Leader only; sixth |
| open | Open time | 0 | Last |

Order rules, stated once. The order is next, since, meetings, replies, risks, team, open. Two moves are allowed, and a moved section goes directly after Since yesterday (Team sweep before Risks when both move): Risks moves when a calendar is connected and shows no sales calls today; Team sweep moves when a leader has no deals of their own and no external meetings. With no calendar connected the order is fixed. A skipped section keeps its id with an `empty` line.

Default `empty` lines: next "Nothing urgent today; the meetings are all that is needed." · since "No buyer replies, stage changes or signatures since the previous working day." · meetings "No sales calls today." (no calendar: "Calendar not connected, so meetings were not read.") · replies "No buyer questions waiting in the last 7 days." · risks "No active risk signal on the deals read." · team "Not shown: no team view." · open "No free block of 30 minutes or more." (no calendar: "Calendar not connected, so open time was not read.")

### next: Next moves

Overdue items first, oldest first, then upcoming items by nearest date, ties by larger amount; an item blocking today's call counts as due before the call and leads the upcoming ones. At most 5. For a clean day, one item whose headline says nothing is urgent and the meetings are all that is needed.

| Field | Content |
|---|---|
| headline | Verb first, names the person: 14 words or fewer |
| meta | Company, deadline or time |
| tags | Optional: "Blocks 2pm call" (warn) |
| detail | One line of reason, 20 words or fewer |
| steps | 2 to 3, each starting with a verb |
| evidence | Promise or fact with date |
| sources | Call, email, or CRM note with date |

Example: headline "Send Tomas the security questionnaire before the 2pm call"; meta "Harbor & Pine Logistics, due 1:30pm"; tags [{"text":"Blocks 2pm call","tone":"warn"}]; detail "Lena promised it on the 9 Oct call and it has not gone out."; steps ["Attach the completed questionnaire to the thread with Tomas", "Confirm in the reply that legal review is booked"]; sources ["Call 9 Oct", "Email thread 15 Oct"].

### since: Since yesterday

| Field | Content |
|---|---|
| headline | 10 words or fewer |
| tags | One of {"text":"Good","tone":"good"}, {"text":"Bad","tone":"warn"}, or "News" |
| sources | Where it was seen |

Example: headline "Quillfeather Studio signed the order form"; tags [{"text":"Good","tone":"good"}]; sources ["Signing tool, 16 Oct"]. Past the cap, add a final grouped item with counts only (for example "4 more team stage moves").

### meetings: Today's meetings

Sales calls only. Vendor, partner, and internal meetings fold into one final item.

| Field | Content |
|---|---|
| headline | Time, company, call type |
| meta | Attendees with titles |
| tags | "First meeting", "New to the deal" (with a profile link in detail, once), or empty |
| detail | Deal line (stage, amount, close date, days since last two-way touch), then last time and what is open in 25 words or fewer |
| steps | Optional single preparation action |
| evidence | Promises and whether they were met |
| sources | Call, email, CRM |

Each item shows five lines or fewer. Example: headline "2:00pm Harbor & Pine Logistics, pilot review"; meta "Tomas Reyes, Head of Operations; Priya Anand, Finance Lead"; detail "Pilot, $48,000, closes 30 Nov, 3 days since last call. Security questionnaire promised, not sent; Economic Buyer not yet on a call."; steps ["Open with the questionnaire status"]. Closing item: headline "Also today: one agency kickoff, three internal meetings".

### replies: Replies waiting

The buyer wrote last in the last 7 days and the message holds a question, request or deadline. Other buyer-last messages belong in Since yesterday.

| Field | Content |
|---|---|
| headline | Name, company |
| meta | Channel, days waiting |
| detail | What was asked, 20 words or fewer |
| sources | Thread date |

Example: headline "Marcus Lindqvist, Copperleaf Foods"; meta "Email, 4 days"; detail "Asked whether SSO is included in the base tier."

### risks: Risks

Worst first: more active signals first, then larger amount; at most 3 per rep shown, the rest in the cap overflow. Close-out candidates (scoring-axes `## Definitions`) are one final note item, headline "Close-out candidates", with company names in detail. A candidate that is also at risk keeps its risk row, tagged "Overdue close date" where its close date has passed; one that is not at risk does not count as a risk.

| Field | Content |
|---|---|
| headline | Company and amount (amount omitted when unknown) |
| meta | Owner, stage, quiet days (null when no contact is recorded) and channel of last contact, for example "12 days, call" |
| tags | Active signal names from Risk signals (warn) |
| detail | The concrete reason in 25 words or fewer, plus "per CRM" if judged on CRM fields only |
| steps | One next action (a verb, who, how, when) |
| evidence | Dates behind each signal |

Example: headline "Willowbrook Dental, $22,000"; meta "Dev Mehta, Proposal, 12 days, call"; tags [{"text":"Deal quiet","tone":"warn"}]; detail "Last buyer reply 6 Oct; the pricing question from that call is unanswered."; steps ["Reply to Ines with the two-tier pricing sheet by Wednesday"].

### team: Team sweep

Leader only. One item per rep, ordered by most risk. The rep name must equal the CRM owner field exactly.

| Field | Content |
|---|---|
| headline | Rep name, as in the CRM owner field |
| meta | Risk count, deals closing this week |
| detail | at most 30 words: whichever single deal or decision calls for the leader |
| children | That rep's risk items, in the format of the risks section |

Example: headline "Dev Mehta"; meta "3 at risk, 2 closing this week"; detail "Willowbrook Dental closes Friday and has gone quiet; an executive introduction would help."

### open: Open time

| Field | Content |
|---|---|
| headline | Start to end, length ("10:30 to 11:45, 75 min") |

One item per free block of 30 minutes or more. No suggestions for using the time.
