# CRM data check: category rules

Run all seven against the guide's own fields and thresholds. Report each as OK or Needs attention with a count. A category that cannot be checked is "not checked" with the reason.

## Close dates

A deal fails when the guide requires a close date and it is missing or earlier than today (honor any grace period set in Data check thresholds). Do not make up a date. Offer one solely where a call or email provided it (say, the buyer named the end of next month on a specific call); in every other case the owner decides, so list it under Open decisions.

## Next steps

A deal passes with a valid next step as defined in scoring-axes `## Definitions`: a calendar meeting with someone on the buyer side, or an open task with a date that has not passed. A deal with no calendar entry (no calendar at all, or a partial one) falls back to its dated next-step field, labelled "per CRM". It fails when none exists, including a next-step field with no date or only dates that have passed. A scheduled meeting passes even when the next-step wording is stale, with a text refresh suggested as a minor fix.

## Required fields

A gap is any required field that is empty: the every-deal fields plus those for the deal's current and earlier stages. Close date, next step, and at least one contact are counted in their own categories, so do not count them again here (a "two or more contacts at this stage" rule is counted here). Skip fields under Fields to ignore and rules for stages the deal has already passed. Check deals lost in the last 30 days for what the guide requires of closed deals, usually a loss reason; without it the team loses its record of why it loses. Tally by field instead of by deal (e.g. "112 of 144 filled"), which stops a single strict stage rule from sinking the category. Name the field most often missing. A required closed-deal field whose column is absent from the data is "not checked"; name the field in the report.

## Stage vs. activity

Compare each deal with Proof by stage in deal-lifecycle: the records, calls, and emails that should exist. Where no proposal artifact exists, use the inferred proof in the guide-build reference. A Proposal with no proposal or price sent, or a Negotiation with no buyer reply in 30 days, fails. State what is absent and recommend the stage the evidence backs. When evidence runs ahead of a deal's stage (say, a call confirmed a pilot yet the deal sits earlier), the deal passes, but propose advancing it, citing that evidence. Do not advance a deal on a hunch. Pulling a deal backward is left to the owner, so route it to Open decisions rather than a change group. Where the read window holds no call, email, or meeting for a deal, judge by CRM record alone; if that is not enough, exclude the deal from this category's count and say how many were excluded.

## Contacts

With no contact data at all (no contact column or records), Contacts is "not checked"; a champion column is a hint only, never a contact record. Otherwise it fails when no contact is linked. If calls or email show the buyer, propose the link. Search the CRM for the person first (by email, then by name and company) before proposing anything new; if found, propose linking the existing record to the deal. New contacts come only from attendees and senders seen in calls, calendar or email; a person only mentioned is not proposed. At most 3 new stakeholders per deal, titled people first.

## Duplicates

With no domain or email data on companies or contacts, Duplicates is "not checked"; say so. Otherwise find companies that share a website domain or have almost matching names ("<Company> Inc" versus "<Company>"), contacts that share an email address, or a same-named person at one company. If Data check thresholds define a matching rule, count only pairs meeting it and list name-only matches as "name match only" without counting them. For each pair, say which record has more deals and activity and should be kept. Merges happen in the CRM by hand.

## Fill from calls and email

For each item in the Capture map, look for the answer: competitor the buyer named, new stakeholders (attendees and senders seen in threads or calls who are not on the deal; at most 3 per deal, titled people first), budget, amount, seat count, timeline, decision process. Each suggestion cites its source and date. Where a field is already filled and a more recent call contradicts that value, suggest the update and display both values; loss reasons are included (say, "timing" logged while the call reveals an in-house build). Loss reason fixes join the calls-and-email group and count here. Amounts come only from the buyer's statements or from a sent quote or proposal, never from internal estimates. When the CRM is missing a next step that a call or email established, propose a follow-up task carrying an owner and evidence, and a due date only when the source gives one (weekday-only dates per scoring-axes `## Definitions`); otherwise omit the due date and say so. Search before proposing any new contact.

## Evidence for every fix

Source and date, with a short quote when the exact words were read, else "Logged: <paraphrase>" (`assets/ref/shared-csv-as-crm.md`), so the person can approve without opening anything. A fix with no source is not a fix; drop it or move it to Open decisions.
