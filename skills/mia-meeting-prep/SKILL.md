---
name: mia-meeting-prep
description: Builds a briefing for one upcoming external meeting that can be skimmed in 60 seconds, for the user's own use and not for the buyer. Not for a buyer-facing agenda (write that directly), a whole day (use mia-daily-sync), or a call that just ended (use mia-call-follow-up); try "Meeting prep for <company>", "Brief me before my 3pm", or "Who's in tomorrow's call?".
---

# Meeting prep

## Shared rules

### Sources and pack files
Try every source (CRM, calls, email, calendar, chat, signing tool, docs, quotes) and name those that answered. Buyer chat is deal activity; check pending contracts' signing status. A CSV standing in for a CRM follows `assets/ref/shared-csv-as-crm.md`.

Read pack files by `##` heading (format in `config/SCHEMA.md`). Look in this order: the `mia-pack/` folder in the working folder, then files attached to or present in the conversation or project, then the `config/` templates, which are defaults and count as seed. Team files outrank personal ones, except voice.md. A file that does not exist is "missing": use defaults and add one closing note that pack setup can create it. A file that exists but is unfilled (`status: seed`, or only template placeholders) is "seed": use defaults for what it lacks, treat its starting values as editable (a seed scoring-axes makes categories "starting values") and add the provisional line.

### Where files live
Workspace mode: you can read and write files in the user's working folder (Claude Code, Codex, other coding agents). Chat mode: you cannot (chat apps). Pick the mode from the tools you have. In workspace mode, write pack files to `mia-pack/` only after the person confirms, save each report as `mia-reports/<skill>-<YYYY-MM-DD>.html` (Markdown when the report falls back), and state the paths. Reports can name deals, so say once to keep `mia-reports/` out of version control. In chat mode, give downloads or copy blocks and keep no history.

### View and scope
Role (rep, leader, both) comes from working-style, where the placeholder `<rep | leader | both>` counts as unset. When unset or absent: an explicit scope, what the user said about themselves in this conversation, else the user's email against CRM owners (most open deals: rep; few while others own most: leader; real share of both: both), else ask once, else rep. State the view at the top. For both, "my deals" gives own deals and "team" the team view; offer the other in a line. A leader with no deals gets the team view. Team scope: CRM team data, roles, then owners of deals touched in 90 days; else list owners.

Sales pipelines only (no onboarding, renewal, support, abandoned); with several, use the pack's or the largest. Last activity is the latest two-way touch on any channel. Before calling a deal quiet, verify outside the CRM field (unanswered mail inflates it; chat never shows), state the channel ("12 days, call"), and tag CRM-only verdicts "per CRM".

### Risk and evidence
Risk means an active signal in the Risk signals table of scoring-axes.md; never write thresholds elsewhere. Its `## Definitions` and `## What counts as evidence` fix every term used here. A contract unsigned 7 or more days is a missed next step. An overdue promise by either side is a signal; name who promised what.

Every fact carries source and date. Unsupported claims and unchecked sources read "unconfirmed" or "not seen", never "missed"; our own notes stay unconfirmed until the buyer backs them. Quote only words read, to the right speaker; a logged summary is no quote.

### Chat reply and offers
Chat reply: the provisional line first (only when a seed file was used); then the skill's items in its own layout, else key numbers and the top items it names; then the first-run line (report skills), the sources line (with any missing-file note and any check skipped because a seed file lacks what it needs, in one clause), one offer, and `Config:`. A skill's layout replaces only the order of its items; key numbers show only if it lists them. Keep it to one screen.

`Config:` plus the files used with versions is the last line. Offer priority: a skill-defined offer, single or ordered pair, first; else a schedule offer; else the most useful next skill not yet run here.

Scheduling: a scheduling tool is any tool that can create a scheduled or recurring task. When one exists and none is set for this skill, offer a schedule at its place in the priority; create it after a yes and never repeat a refusal. With an attached or pasted CSV as the data, say nothing about scheduling anywhere and make no schedule offer, a skill's own included. With other data and no scheduling tool, say once that a scheduler can repeat the run.

### Failures and style
Retry a failed call once, continue, mark partial totals. No CRM: follow `assets/ref/shared-csv-as-crm.md` (it covers the CSV request and the light fallback). A skill's read caps apply to records. No amounts: count deals.

Facts and next actions only; no encouragement, no emojis. Every flag gets a reason and an action, in the user's terms. Describe work, not people: no scores, rankings or personal adjectives; show good habits. Leader output is shareable; personal files never feed team totals.

Report skills also read assets/ref/shared-reports.md.
Skills that write or draft also read assets/ref/shared-writes.md.

Before step 1, read assets/ref/shared-reports.md.

## Purpose

Turn what is known about one meeting into preparation. The page is a private briefing, never a document for the buyer; if asked for an agenda, decline this skill. It is read-only: no CRM updates, sending, drafts, or schedule creation before the user says yes. Every section is optional. A first meeting with three sections is a complete result, and an empty section is dropped, not padded.

## Find the meeting

Never stop to confirm a single match. A round trip just before a meeting is where people give up.

1. Search the calendar for meetings with the named company in the next 14 days and match each to a CRM deal.
2. One meeting: proceed and state in the header which meeting was chosen, so a wrong pick is visible.
3. Several meetings on one deal: prepare the nearest and mention the later ones in one closing line.
4. Distinct deals or divisions inside a single company (two business units, say): ask which is intended, listing date, time, attendees and deal for each option on its own line. Only here is a question permitted.
5. No company named: prepare the next sales call today or on the next working day.
6. Leave out meetings with vendors, partners, agencies, recruiters and personal matters, with one exception: a partner or customer arriving via a sales or demo booking link counts as a sales call. Close with one line stating what was left out. A rep view prepares only deals the user owns, a leader view any; meetings on other reps' deals are left out and named in `howBuilt` as "owned by another rep".
7. When the named company is a partner or a vendor (meaning it supplies the user, or does not purchase from them), state this beneath the header and produce just a brief meeting note: attendees, open matters on each side, what to obtain. Drop both the deal section and the qualification ones.
8. Nothing found: offer two lines of probable reasons (the invite carries another name, the calendar is not visible, the meeting is not yet scheduled), then request the buyer's name or meeting particulars.
9. No calendar: ask in one line for date, time, and attendees, or proceed from a supplied `meeting_date` and notes.

## Read plan

Read widely, then keep only what helps this meeting.

- CRM: the deal record, with its owner, source, next step, close date, amount, stage and any filled custom fields; every attendee's contact record; notes and the 15 latest activities; and the form submission behind the contact's creation.
- Calls: summaries of every earlier call with this company, however old, plus the full transcript of the latest one or two. Preparation accumulates: the first calls hold the original goals, the definition of success, and early doubts that matter in every later call.
- Email: threads with each attendee over the previous 90 days, read in full, including answers from copied teammates and emails the deal owner recorded in the CRM. Before marking something owed, confirm no teammate already replied. For a first meeting, study the booking thread with care, since buyers often set out goals and timing in it and later forget.
- Chat: direct messages exchanged with attendees, plus internal threads concerning the deal.
- Contracts: documents waiting and their signing status.
- Web: a short look at attendees with no CRM or call history (role, tenure). Company news only when it ties to something the buyer said matters.

Then settle two facts. The meeting number (the Nth real meeting with this buyer; when earlier meetings are not logged, write "Meeting N or later (n logged)") and whether buyer-side material already exists (booking form, intro reply, SDR handoff note, earlier call). A first meeting with a submitted form is not a blank page.

## Hold it against the pack files

This step turns a summary into preparation.

- deal-lifecycle, Qualification to close: judge each element at the current stage as known, partly known, or unknown from evidence. The unknowns that matter at this stage become Still unknown, for example "Economic Buyer unknown; only the champion has been on a call." If the file is missing or seed, use standard discovery gaps (budget, decision maker, timeline, problem, competition) and say so.
- working-style, Moves from my best deals, and winning-plays: suggest the one move that fits this meeting. Recurring slips: flag the ones that apply to this deal.
- buyers-and-competition, Competition: if a competitor surfaced, state how the team wins and loses against it.
- scoring-axes, Risk signals and Definitions: if the deal is a Deal at risk, say so in the header with the reason; dates and Economic Buyer follow the Definitions.

## Sections

Use exactly these names, in this order: Why this meeting, Who's in the room, Their goals, Since your last call, Still unknown, Talking points, Watch for, Buyer's words. The header (company, time, length, meeting number, deal, stage, amount, close date, and the reason if the deal is a Deal at risk) goes above them. Read assets/schemas/mia-meeting-prep.md at run time for what each section holds, its caps, and word limits.

Rules that decide content:

- Who's in the room: flag New, Skeptic (with the quote, or a Logged line), Champion (point to the moment), or Economic Buyer (what the person did on a call, never the title alone; "per CRM, unconfirmed" when only a CRM role backs it) only when evidence supports it. A wrong Champion label is worse than none. When someone is unidentified, mark that and recommend the host be asked who the person is.
- Since your last call: check both sides, for example "Promised the pricing sheet by Tuesday: sent" or "not sent".
- Still unknown: write each item so it can be asked in the meeting.
- Talking points: each names an outcome to walk away with (a yes, a number, a name, a date) and never a subject area ("pricing discussion") or a method. If the buyer asked for a look at something, it usually goes first. Link every point to a gap, a requirement of the stage, or something the buyer requested.
- Watch for: risks that have a source only (a long silence, a CRM close date that disagrees with the buyer's, a new stakeholder, a missed promise, a competitor), each with a handling tip. Slip is a forecast flag and is not used here.
- Their goals and Buyer's words: exact words only; with logged summaries alone follow `assets/ref/shared-csv-as-crm.md`. Buyer's words is omitted when no exact phrases exist.
- Number tiles: Gaps (Still unknown items) and Open promises (items tagged Open in Since your last call). Every factual row carries a source: call, email, or CRM note, and when.

## Special cases

- First meeting with no buyer-side material: write only the header, Who's in the room, Talking points, and Still unknown, and state "First meeting, no prior touchpoints."
- Leader preparing a rep's meeting: use the section note for whose deal it is and a gap or decision only the leader can unlock (an executive introduction), 25 words or fewer. For a vendor or partner meeting, say that in the note.
- No CRM: rely on the calendar, email and calls; leave stage and amount unknown instead of guessing; add one closing remark that gaps sharpen once the CRM is connected or the deal record is pasted.
- A source fails: retry once and note it in one line.

## Length and rules

Visible rows total about 450 words; the rest goes in detail. Facts and questions only, no encouragement.

## Chat reply

Layout: the meeting and the single most important thing about it. First-run line: a short orientation. Sources line: any missing source or skipped meetings. Offer: when a scheduling tool exists and no Meeting prep schedule is set, preparing each external meeting every weekday at 7:00 (on a yes, create it and confirm in one line); otherwise that after the meeting, "Follow up on my last call" prepares the follow-up and CRM notes with this context.
