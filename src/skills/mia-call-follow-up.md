---
name: mia-call-follow-up
description: Turns one sales call that just ended into a follow-up email draft, a CRM change proposal, and dated tasks, with CRM writes only after approval. Not for cleaning up many deals in the CRM (use mia-crm-data-check) or nudging a quiet deal (use mia-next-move); try "Follow up on my last call", "Draft the recap for the Northwind call", or "Update the CRM from that call".
---

# Call follow-up

{{SHARED}}

Before any draft or change, read assets/ref/shared-writes.md. If the follow-up is also kept as a report, read assets/ref/shared-reports.md before building it.

## Purpose

Keep round trips to a minimum. The output is a working document in the chat, in Markdown, not a report. If the user wants to keep it, also build it as a report using the same sections in the same order. Email is drafted, never sent.

## Find the call

Do not ask which call unless you truly cannot tell.

1. A pasted transcript or notes are the call. Take company and attendees from them. If no names appear and no deal matches, the shared placeholder rule applies to [Company] and [Buyer].
2. Otherwise look in the call-recording tool or on the calendar for outside calls finished within the past 48 hours, widening to 7 days when none turn up, narrowed by company or date.
3. One clear candidate (the latest external call, or the company's only call): proceed, and name the call in the call line. When a calendar entry conflicts with the call record (time, attendees, company), trust the call record and flag the conflict in one line.
4. Several equally likely candidates (two buyer calls within one hour, no company named): list each on its own line and ask which. This is the only confirmation to request.
5. No result: report where it searched, then request a transcript, notes, or the company name. Never reconstruct a call it cannot see.

## Read plan

- Complete transcript of the call at hand.
- Up to 3 earlier calls with this buyer, as summaries.
- The CRM deal record and its contacts, plus the 10 most recent activities or notes.
- Email: at most 10 threads involving the attendees.
- Chat, only when connected and only for this buyer.

Extract: what the buyer called important, objections, rivals and tools named, money and timing remarks, people mentioned, each commitment by either side (owner, action, deadline), and the precise next step.

Look at earlier contact. If something was already promised or sent, build on it, never repeat it. Today's next step replaces an earlier one. Check the deal's recorded emails and post-call activity as well as the user's inbox, since a teammate may have sent the recap.

Match the deal by company and attendee email. Collect stage, amount, close date, next step and any other field the call may settle, with exact field names and permitted options (stage list, competitor pick list), so the proposal uses the CRM's own terms.

## Pack files

| File | Headings | Used for |
|---|---|---|
| voice | Writing patterns, Situation samples (recap after a demo, first follow-up), Signature phrases, Avoid | Writing the email as the user |
| deal-lifecycle | Pipelines and stages, Qualification to close, Proof by stage | Whether the call earns a stage move; method gaps |
| buyers-and-competition | Competition | Competitor names, and the company site for resources |
| working-style | Moves from my best deals, Standing rules | Add a joint plan if won deals had one after the demo |
| scoring-axes | Definitions | Date, next step and open request terms |
| crm-guide | Fields by moment, Capture map, Required fields, Fields to ignore | Which fields to update, where each fact goes, what to leave out |

The crm-guide is the team's agreed way of using the CRM, so its field names and rules outrank your own reading of the CRM. If voice is missing or seed, write plainly and briefly, and say so above the draft.

## Email draft

Write as the user: greeting, sign-off, length, structure, and phrases from voice.

- Open with something specific the buyer said. Quote only words that were read, and attribute them to the person who said them; a person merely mentioned on the call did not speak. From logged summaries alone, paraphrase without quotation marks (`assets/ref/shared-csv-as-crm.md`).
- Confirm the next step with an owner and a date. Make one request.
- Deliver what was promised and can go now (a link, an answer), or say when it will arrive.
- Mention price only when it came up on the call or voice or working-style says recaps state it; take figures only from the pack or CRM, never invent discounts or terms.
- Recipients: only people and addresses seen in the call, calendar, CRM, or email; an address never seen is a placeholder.
- When a recap was already delivered, by the user or a colleague, skip another; name the sender and time, and draft only the missing material.
- 200 words or fewer, unless voice shows longer recaps. It should be ready to send; placeholders follow the shared rule.

## CRM changes

Include only fields the call or today's email clearly supports, following crm-guide when it exists. Read assets/ref/mia-call-follow-up-crm-fields.md at run time for the list of change types (next step, stage, close date and amount, competitor, qualification fields, tasks, call note, new contacts) and the rule for each.

Show changes as a table (field, current, new), then the tasks as a dated checklist. With a write tool, ask a single time whether the N changes should be applied and the N tasks created; the pause matters, since a wrong stage or guessed competitor alters the forecast teammates see. After approval, carry out only what was approved; the next reply is the apply result (what saved). With no write tool (a CSV counts as none) or no CRM, ask no approval question: give the changes and tasks as a copy block and use the shared offer priority.

## Resources and gaps

Resources to send appear only when the buyer asked for something and a real page on the user's website answers it. Search the site and give the actual URL. If nothing fits, write that they asked for X and it was not found. If nothing was requested, drop the section.

For the next meeting: up to 3 things the deal still needs against the method and stage (decision maker not named, budget not discussed), each with the question to ask.

## Output layout

In this order:
1. Call line: the call used (company, date and time, attendees, source of the call), plus any calendar conflict line.
2. Summary: 3 to 5 lines on what happened, what changed and the next step; the same text is the CRM call note.
3. Follow-up email: Subject, To, Body, with a line above it for placeholders or an earlier recap.
4. CRM update, titled with the CRM and deal: the change table, Tasks, new contacts, and one line "add when seen" naming people only mentioned on the call.
5. Resources to send, only if requested; then For the next meeting: gaps and questions.
6. The approval question (with a write tool). It is this skill's offer. Without one, the offer is the shared priority, led by Meeting prep for the next meeting on this deal if the calendar shows one, else Next move for another deal that came up.
7. The `Config:` line, last.

## Special cases

- No call-recording tool: ask in one line for a transcript or notes. A calendar entry alone cannot support a recap.
- No CRM: copy block with common field names (next step, stage, close date, competitor, task), no approval question; mention connecting a CRM once.
- No matching deal: produce the email, note and tasks, and when the call was a genuine sales discussion, propose creating a deal using the fields displayed.
- Existing deal but no earlier emails visible: do not assume anything was sent; say so in one line.
- A leader joined a rep's call: when the rep owns the deal, ask no further questions, write the follow-up on behalf of the person who ran the call, and state who that is. Tasks for the rep list the rep as owner. When a team-standards file containing Every deal gets exists, include a line noting what the rep handled well or skipped relative to it.
- A call that is internal or not about sales: flag that, and propose just a note and tasks.

## Rules

Include only what has a source. A made-up commitment or CRM field filled by guesswork costs more than an empty one; leave it out and list it among the gaps for the next meeting. Never send or write without approval. Write in the user's voice. Keep buyer details out of any saved pack file, since the CRM record is the right home for deal details. No commentary such as praise for the call. The deliverable is a document, not coaching.
