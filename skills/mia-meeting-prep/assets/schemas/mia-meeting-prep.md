# Meeting prep: DATA section map

Fill the DATA object in assets/report-shell.html and change nothing else in the shell. Use the same section order every time. Every section is optional: omit a section that has no real content instead of padding it, and do not show a heading that says "none". This is the one schema that omits empty sections, so it has no `empty` texts. Never write "you" or "your" in DATA, apart from the fixed section titles and quotations. Refer to people by first name. The page is a private briefing and is never sent to the buyer.

## Top-level keys

| Key | Content |
|---|---|
| meta | `title` "Meeting prep: <company>", `skill` "mia-meeting-prep", `generatedAt`, `view` (the header line: time, length, meeting number, deal name, stage, amount, close date, and the Deal at risk reason if any), `firstRun`, `readCounts` (calls, emails, CRM records read) |
| provisional | Seed line when any file used has `status: seed`; otherwise empty |
| numbers | Gaps (count of Still unknown items) and Open promises (count of items tagged Open in Since your last call) |
| sections | Those present of the eight below, in this order |
| howBuilt | What was read, anything that could not be read, any check skipped for a seed file, and meetings left out as "owned by another rep" (60 words or fewer) |
| whyFree, readiness, readinessUrl | From assets/readiness-line.md |
| config | Files used with versions |

Make the header unmistakable about which meeting was chosen, and add the meeting number (real meetings only; "Meeting N or later (n logged)" when earlier meetings are not logged). For a first meeting with no buyer-side material, write "First meeting, no prior touchpoints" as the first section's `note`, and include only Who's in the room, Talking points, and Still unknown. For a vendor or partner, say so in `meta.view`, and build only a short brief (attendees, what is open on both sides, what to get). Every fact row has `sources` saying whether it came from a call, email, or CRM note and when.

When a leader prepares a rep's meeting, put a note of 25 words or fewer in the first section's `note`: whose deal it is and the gap or decision the leader can unlock.

## Sections

| id | title | cap |
|---|---|---|
| why | Why this meeting | 3 |
| room | Who's in the room | 0 (everyone attending) |
| goals | Their goals | 5 (minimum 3 when present; fewer when evidence is short, see below) |
| last | Since your last call | 4 |
| unknown | Still unknown | 4 |
| points | Talking points | 4 (minimum 2) |
| watch | Watch for | 3 |
| words | Buyer's words | 5 (minimum 3; fewer when only 1 or 2 exact phrases exist; omit if none) |

### why: Why this meeting

| Field | Content |
|---|---|
| headline | The agenda item or what the buyer wanted covered, 20 words or fewer |
| sources | Where it was said |

Example: headline "Walk through the pilot rollout plan for the two Ohio sites"; sources ["Email from Priya, 14 Oct"].

### room: Who's in the room

| Field | Content |
|---|---|
| headline | Name, title |
| meta | Role in the deal and what the person cares about, 12 words or fewer |
| tags | New, Skeptic, Champion, Economic Buyer (Skeptic as warn, Champion and a proven Economic Buyer as good); "Economic Buyer, per CRM, unconfirmed" (no tone) when only a CRM role backs it, per scoring-axes `## Definitions`; only flags that evidence supports |
| detail | For an unknown person: "Unknown; ask the host who they are" |
| evidence | Skeptic: the quote, or "Logged: <paraphrase>". Champion: the moment. Economic Buyer: what the person did on a call, or "per CRM, unconfirmed" |
| sources | Call, email, CRM, with date |

Example: headline "Rafael Duarte, VP Finance"; meta "Approves spend; wants payback under 12 months"; tags [{"text":"Economic Buyer","tone":"good"}]; evidence ["Asked for the payback model on the 2 Oct call and named the 30 Nov budget cutoff"]; sources ["Call 2 Oct"].

### goals: Their goals

Built up over all touchpoints, using the buyer's phrasing wherever possible. With fewer than 3 goals backed by evidence, show those and state the count in the section `note`; logged summaries follow `assets/ref/shared-csv-as-crm.md`.

| Field | Content |
|---|---|
| headline | The point, 8 words or fewer |
| detail | The quote in quotation marks, or "Logged: <paraphrase>" when only a logged summary exists |
| sources | Call, email, or form, with date |

Example: headline "Cut manual scheduling time"; detail "\"Right now two people spend Mondays on the roster.\""; sources ["Call 18 Sep"].

### last: Since your last call

| Field | Content |
|---|---|
| headline | 12 words or fewer, including who owes what and by when |
| tags | "Done" (good), "Open" (warn), "Open request" (a buyer request not yet answered; a gap, not our promise), or none; Open means a promise either side still owes. A buyer promise known only from our own summary reads "unconfirmed" |
| sources | Where seen, with date |

Example: headline "Pricing sheet promised for Tuesday: not sent"; tags [{"text":"Open","tone":"warn"}]; sources ["Call 2 Oct; no sent email found as of 15 Oct"].

### unknown: Still unknown

Most important at this stage first. Each item is written so it can be asked in the meeting.

| Field | Content |
|---|---|
| headline | The question, naming the element |
| detail | Why it matters at this stage, one line |
| sources | The stage requirement that makes it matter (deal-lifecycle) or the gap source |

Example: headline "Who signs the order form besides Rafael?"; detail "Pilot stage requires the Economic Buyer's approval path to be named."; sources ["deal-lifecycle, Qualification to close"].

### points: Talking points

Each is an outcome to carry out of the meeting (a yes, a number, a name, a date), neither a topic nor an approach.

| Field | Content |
|---|---|
| headline | The outcome, 8 words or fewer |
| detail | The gap, stage requirement, or buyer request it comes from |
| steps | 2 to 3, how to get it in the meeting, each starting with a verb |
| sources | Link to the gap or request |

Example: headline "Decision date agreed for the pilot"; detail "Close date of 30 Nov has no buyer-stated process behind it."; steps ["Ask Rafael which approvals come after the pilot review", "Offer 12 Nov as the checkpoint and ask for a yes"].

### watch: Watch for

| Field | Content |
|---|---|
| headline | The risk (competitor named, missed promise, new stakeholder, CRM close date that disagrees with the buyer's date, long silence); Slip is a forecast flag and is not used |
| detail | How to handle it |
| sources | Required; no risk without a source |

Example: headline "Brightwave named as the alternative"; detail "Ask what Brightwave covers that the pilot scope leaves out before the buyer raises it."; sources ["Call 2 Oct"].

### words: Buyer's words

Exact phrases only, from a call or email read in full. Omit the section when no exact phrase exists; a logged summary is never shown here.

| Field | Content |
|---|---|
| headline | The phrase in quotation marks |
| meta | Speaker, by name |
| sources | Call or email, with date |

Example: headline "\"We can't run another quarter on spreadsheets.\""; meta "Priya Anand"; sources ["Call 18 Sep"].
