# Pack setup: summary and file contents

## Summary layout by role

Order the lines from what the person would least expect to what they would confirm at a glance. Quote briefly where it helps.

Rep: how many of their own deals and the main segment; what they sell, to whom, at what amount and cycle; how they qualify and what usually goes missing; how they run calls, with one short real quote; the feel of their email in two or three words, with greeting, sign-off, and length; one phrase that sounds like them; two or three behaviors from the best deals and the move most often missing on the rest; what works, with counts.

Leader: team size and whether the leader carries deals; open deal count, average amount, and cycle; the real process (stage flow, where deals stall and why); the method in use and what reps fill or skip; what reps did on the best deals, and the standout habit with counts on both sides, using no ranking words; why the team wins or loses against each competitor; one unexpected team-level pattern.

Both: open with a rep line and a team line. Give three or four lines on the person's own voice and deals, two or three on the team, eight lines at most.

## The two questions

Pick the types that fit what you found. Each must name a concrete fact.

- Resolve a conflict in the data: "9 deals sit in Proposal and 6 have no proposal on file. Is Proposal really the pricing conversation?"
- Test a rule before it is written down: "Price never goes out before a second call. Is that always true?"
- Choose between real options: "Two recap styles are in use on the team. Which one should the team follow?"
- Ask for something only the person knows: "4 of the 6 losses to a rival came right after a security review. Is security the deciding factor?"

No generic questions. If the data answers a question, skip it. If a source was empty, name the line it changed and how to fix it ("no email was visible, so the voice is a guess").

## Files

Use the headings from `config/` templates exactly, so other skills can find sections by name. Tag factual lines inline with `[crm n=..]`, `[calls n=..]`, `[email n=..]`, `[stated]`, or `[inferred]`; the frontmatter carries no tags.

| File | Approx. size | Content |
|---|---|---|
| deal-lifecycle | Short tables | Real stage names, typical days, share that moves on, entry proof observed from activity |
| buyers-and-competition | Short | Titles, company types, trigger events, offer and price ranges, one block per competitor named in the data |
| market-physics | Short | Patterns with counts; if fewer than 5 closed deals, write "too little history" and leave sections empty |
| winning-plays | One block per play | Run it when, the moves, the Answers signal line, seen on n of m won deals; leave Close rate when run blank |
| team-standards | Short | Leader or both only; Every deal gets and Team shape filled from observed practice; Target for the period stays empty unless stated |
| voice | 1,000 to 1,800 words; none with no emails written by the user | Register, patterns, situation samples with quotes, signature phrases, reply signals if earned, Avoid |
| working-style | 200 to 500 words | Profile with role, then the evidence-built sections; for a leader with no deals, only what the evidence supports, other lines "not seen" |

For scoring-axes, copy the template, fill only frontmatter `owner` and `updated` and the `<amount range>` when the data supports it, and keep every other value as shipped; stage names go in deal-lifecycle. Each generated file keeps the template's current version and gains one Changelog line, "filled from data on <date>". Plays should name the risk signal they answer using the signal's name in scoring-axes.
