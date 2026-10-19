---
file: crm-guide
scope: team
version: 0.1.2
updated: YYYY-MM-DD
owner: <RevOps or Sales Manager>
status: seed
---

# CRM guide

How your CRM is used in practice, so that skills update the right fields and checks do not flag fields nobody uses.

## Pipelines in scope

The CRM, the pipelines it holds, their stages in order, and whose deals are in scope.

## Fields by moment

| Moment | Fields to update | What goes in them |
|---|---|---|
| Right after the first conversation | | |
| Right after any later conversation | | |
| When a milestone is reached (demo, proposal, close) | | |

## Required fields

Field names exactly as the CRM shows them, and what counts as filled. Add a second table for fields required only from a certain stage.

## Fields to ignore

Fields present in the CRM that nobody fills in.

## Allowed values

For each field limited to a fixed list, such as competitor, source, stage, or reason for a loss, copy the choices exactly as the CRM spells them. Note any topic that has no field at all.

## Capture map

What a call or email can tell us, and the exact CRM field each item belongs in: competitor named, new stakeholder, amount or seat count, buyer timeline, decision process. Where a field takes a fixed list, the exact options live under Allowed values. If a topic has no field, say so here.

## Forecast fields

The fields forecasts read: the one holding the rep's commit call, the amount, the close date, and the owner. If your CRM keeps the commit call in a custom field, write its exact name here.

## Data check thresholds

The limits the checks use: how overdue a close date must be before it is flagged, any limit on next steps beyond the valid next step in scoring-axes `## Definitions`, and the rule for spotting duplicate records.

## Changelog

- 0.1.2 (YYYY-MM-DD): what qualifies as a next step now points to scoring-axes Definitions
- 0.1.1 (YYYY-MM-DD): added Capture map
- 0.1.0 (YYYY-MM-DD): seed created
