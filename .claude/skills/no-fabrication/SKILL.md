---
name: no-fabrication
description: Enforce provenance rules on every claim before delivery — every number, name, date, title, dollar figure, percentage, scope claim, or accomplishment must trace to a sourced line in a reference document (e.g., master-cv.md, source data file) or to an explicit user confirmation in the current conversation. No "creative interpretation" tier, no "implied by other facts" tier. Produces a provenance map appended to the deliverable that pairs each claim with its source. Use whenever an agent is making factual claims that will reach an external audience — resumes and cover letters, pitch decks, marketing copy with statistics, policy briefs, written work of any kind. Auto-invoke before any draft with quantified claims ships. Red flags that trigger source re-check: round large dollar figures, suspiciously clean percentages, broader scope than source, timeline claims not in source, titles or awards not in source.
---

# No-Fabrication Protocol — Provenance Requirements

> Every claim that lands in an external-facing deliverable traces back to a source line in a reference document or to the user's explicit confirmation.

---

## THE CORE RULE

**No claim ships without a source.** If the agent cannot cite a specific line in a reference document (or a confirmation message from the user in the current conversation) for a number, name, date, or accomplishment, that claim does not appear in the deliverable. There is no "creative interpretation" tier. There is no "this is implied by other facts" tier. Every claim is either sourced, or omitted.

For resume and cover-letter work, the source-of-truth document is `.claude/agents/pitch/master-cv.md`. For other deliverables, the source is whatever reference file or data set the user has supplied.

---

## PROHIBITED FABRICATIONS

The following are never invented under any circumstance:

- **Quantified metrics** — dollar amounts, percentages, headcounts, time savings, deal sizes, customer counts, geographic scope, transaction volumes
- **Dates** — start / end dates of roles, project timelines, certification dates
- **Titles** — exact job titles, level identifiers (IC6, VP, Senior, etc.)
- **Company names** — including subsidiaries, business units, vendor partners
- **Customer / client names**
- **Technology names** — specific tools, systems, or platforms not already in the source
- **Awards / certifications**
- **People mentioned** — mentees, direct reports, manager titles
- **Methodologies / frameworks claimed** — only those the user has actually applied per the source

If the request asks for evidence of something the agent cannot source, the agent flags it and asks the user instead of inventing a plausible-sounding equivalent.

---

## ALLOWED LANGUAGE-LEVEL TAILORING

The agent may, without re-asking the user:

- Reorder bullets to put request-relevant achievements first
- Trim bullets to fit page or align focus (without altering metrics or facts)
- Substitute synonyms when the request uses different vocabulary for the same concept (e.g., "supply chain orchestration" ↔ "logistics coordination", as long as the underlying activity is the same in source)
- Promote a verified bullet from the bank into the production deliverable
- Combine two bullets that describe related work, as long as no fact crosses between them
- Reword phrasing for tone or clarity, without inventing
- Adjust positioning language using alternates already listed in the source

---

## SOURCING CHECK — RUN BEFORE EVERY DELIVERY

For every claim in the drafted deliverable, build a provenance map:

| Claim in deliverable | Source line in reference | Verified |
|---|---|---|
| _(exact text of claim)_ | _(file > section > line reference)_ | ✓ |

This map is **always included as the last section of the deliverable**, labeled "PROVENANCE MAP — DO NOT INCLUDE IN SUBMITTED [DELIVERABLE]". The user reviews this section to confirm before submitting.

If any row in the provenance map shows a missing or weak source, that claim does not ship. The agent either:

1. Replaces it with a sourced alternative from the bank, OR
2. Cuts it entirely, OR
3. Asks the user to confirm a specific fact before using it

---

## PRE-DELIVERY CHECKLIST

The agent runs through this before declaring any draft complete:

- [ ] **Identity check**: name, location, phone, email, LinkedIn — all match source exactly
- [ ] **Role-by-role check**: every company name, title, location, and date matches source exactly
- [ ] **Metric audit**: every numeric claim ($, %, headcount, time, scope) is verified against source. List any unverified metrics for the user before delivery.
- [ ] **Title-level claim audit**: any "VP", "Senior", "Owner", "Lead" claim is verified against source
- [ ] **Award / cert audit**: every award and certification appears in source (or a user-confirmed addition)
- [ ] **Education audit**: institution, degree, graduation year all match source
- [ ] **Provenance map populated**: one row per claim, source cited
- [ ] **Companion documents (if drafted)**: every claim in companion documents (cover letters, decks, memos) also passes the audit

---

## WHEN THE USER ASKS TO ADD SOMETHING NEW

If the user says "add this" mid-conversation:

1. The agent records the new fact in the conversation provenance log: "Added by user on [date]: [exact wording]"
2. The agent immediately offers to write the new fact into the source-of-truth file (e.g., `master-cv.md`) so it persists for future sessions. The user confirms or declines.
3. The new fact gets a provenance map row citing "user (this session)" until it is committed to the source file.

This way, every new claim has a source — either a file or an explicit user message — and the source-of-truth grows organically over time.

---

## WHEN A METRIC LOOKS WEAK

If the source has a metric that's vaguely worded or incomplete (e.g., "saved time" without a number, "reduced workforce" without specifying how much), the agent:

1. Flags the weakness in the fit summary (e.g., "Bullet on X role mentions promotion but lacks a metric — consider quantifying for next revision")
2. Either uses a softer phrasing that doesn't claim a specific number, OR
3. Asks the user for the number before using it

Never invents a number to fill the gap.

---

## RED-FLAG PATTERNS THAT SUGGEST FABRICATION

If a draft contains any of the following, the agent stops and re-checks the source:

- A round, large dollar figure (e.g., "$10M", "$1B") not present in source
- A percentage that's suspiciously clean (e.g., "improved efficiency by 40%") without a source line
- A scope claim ("globally", "across 50 countries") that's broader than what source describes
- A timeline claim ("in just 3 months") not present in source
- A title or level not in source
- An award / certification not in source
- A first-person achievement that wasn't actually owned by the user (e.g., crediting the user with a team-led initiative they supported but didn't lead)

If any of these appear, the agent removes them and replaces with sourced content.

---

## EXAMPLE OF A CORRECTLY SOURCED PROVENANCE MAP

```
PROVENANCE MAP — DO NOT INCLUDE IN SUBMITTED RESUME

| Bullet on resume | Source | Verified |
|---|---|---|
| Led a multi-site transformation program across [N] locations. | master-cv.md > [Employer] > Master Resume bullets, line 1 | ✓ |
| Reduced cycle time from [baseline] to [result] by redesigning [system/process]. | master-cv.md > [Employer] > Master Resume bullets, line 2 + Source-of-truth metrics row "[metric name]" | ✓ |
| Automated [workflow] covering [$X] in annualized spend. | master-cv.md > [Employer] > Verified bullets bank > [initiative] | ✓ |
| Generated [$X] pipeline within [timeframe]. | master-cv.md > [Prior employer] > Source-of-truth metrics row "[metric name]" | ✓ |
| Reduced regional overhead costs by [X]% through [system/process] integration. | master-cv.md > [Prior employer] > Source-of-truth metrics row "[metric name]" | ✓ |

UNSOURCED CLAIMS NEEDING CONFIRMATION FROM USER:
(none in this draft)

WEAK SOURCES:
(none in this draft)
```

---

## CHANGE LOG

- Protocol created for resume / cover-letter work, then generalized for any claim-making deliverable.
