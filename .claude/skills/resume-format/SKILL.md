---
name: resume-format
description: Reference the user's master resume template and preserve its exact visual format. Use whenever Pitch generates a Word resume or cover letter; read the template path from master-cv.md or user-provided source files, mutate the template in place, and visually verify the output. Covers section order, ATS-safe formatting, template mutation, cover-letter matching, and file naming with spaces instead of underscores.
---

# Resume Format Reference — Match the Master Resume Exactly

> Run this skill every time the deliverable is a Word resume. The output must be visually identical to the user's master resume `.docx`. Only the *content* changes per application — the format never does.

---

## SOURCE OF TRUTH

The reference template is the user's master resume `.docx`. Its path is recorded in `.claude/agents/pitch/master-cv.md` under the **VERIFICATION SOURCES** section (or is provided directly by the user). When in doubt, open the current master resume template and match it exactly.

The master file defines the format. Do not impose a format from this skill that the master doesn't use — open the master, inspect its font, margins, sizes, and spacing, and match whatever it actually does.

---

## STRUCTURE (top to bottom)

This is a common, ATS-friendly order. Match the master's actual order if it differs.

```
1. NAME (large, bold, centered or left)
2. CONTACT LINE (City, State • phone • email • LinkedIn URL)
3. POSITIONING TAGLINE (e.g. "Business Transformation & Applied AI Leader")
4. PROFESSIONAL SUMMARY (one paragraph, 4–6 sentences, tailored)
5. SIGNATURE ACHIEVEMENTS (5 bullets, top-hits, tailored)
6. CORE COMPETENCIES (single line, pipe-separated, tailored to JD vocabulary)
7. PROFESSIONAL EXPERIENCE (reverse chronological)
 For each role:
 - Company name, City, State + Date range (start – end)
 - Title
 - 3–6 achievement bullets, tailored
8. SELECTED APPLIED AI PROJECTS (optional — include if relevant to JD; this can be a hidden differentiator)
9. ACADEMICS (degrees + dates + institutions)
10. TECHNICAL SKILLS (single line, pipe-separated)
```

Some roles or applications may also include a CERTIFICATIONS line, AWARDS line, or LANGUAGES line — add only when relevant to the JD.

---

## TYPOGRAPHY

Match the master file's exact font choices and sizes — open it and inspect. Whatever font, point sizes, margins, and spacing the master uses, the tailored resume uses the same. Do not substitute a different font or change the margins.

General reference points (defer to the master where it differs):

- **Name:** ~16–18pt, bold
- **Section headers:** ~11pt, bold, ALL CAPS (with or without a horizontal accent line, per the master)
- **Job titles within Experience:** italic, ~11pt
- **Body text:** 10.5–11pt, professional serif or sans-serif (whatever the master uses)
- **Contact line:** ~10pt, single line, bullet separators (•)
- **Tagline:** italic or bold-italic, ~11pt

---

## SECTION-BY-SECTION RULES

### Header
Single line of contact info. Format: `City, State • phone • email • LinkedIn URL`

Example: `[City, State] • [phone] • [email] • [linkedin URL]`

### Positioning tagline
Sits below contact line. One short phrase that names the target role family.

Example: `Business Transformation & Applied AI Leader`

Tailor this per JD. If applying to a Director of Operations role, the tagline becomes "Operations & Transformation Leader" or similar — pulled from the alternates listed in `master-cv.md`.

### Professional summary
4–6 sentence paragraph. The opening sentence should name the target role family and core years of experience. The body covers the main impact areas. The close adds a differentiator (graduate program, language fluency, cross-industry, etc.).

The default summary in `master-cv.md` is the starting point. Adjust the opening clause and any keyword emphasis per JD.

### Signature achievements
Five bullets. Each bullet:
- Starts with a strong action verb (Led, Built, Achieved, Generated, Reduced — never "Spearheaded", "Championed", "Leveraged")
- Includes a specific metric ($, %, scale, headcount, time)
- Is one sentence, ~20–35 words

The five bullets are chosen and ordered to match what the JD weights most. Reorder per application; don't keep the master order by default.

### Core competencies
One line, pipe-separated. ~10–15 items. Pull from `master-cv.md` and reorder to put the most JD-relevant items first. Use the JD's exact vocabulary where possible (for ATS keyword matching).

### Professional experience
Reverse chronological. Each role:

```
Company, City, State Mon YYYY – Mon YYYY
Title (italic)
- Achievement bullet 1 (verb-led, quantified, business outcome)
- Achievement bullet 2
- Achievement bullet 3
[etc, 3–6 bullets per role]
```

Format conventions (match the master):
- Company name on line 1, dates right-aligned on the same line
- Title on the next line, italic
- Bullets follow

The most recent role gets the most bullets (4–6). Older roles can be trimmed to 2–3 bullets if not directly relevant to the JD.

### Selected applied AI projects (optional)
Include this section when the JD touches AI, automation, GenAI, transformation, or innovation. This can be the differentiator that makes the user stand out from typical candidates.

Pull project content from `master-cv.md`. Add or substitute new projects as the user ships them.

### Academics
Lines of degree + institution + date, no bullet detail unless GPA was 3.5+ or there's an honor worth noting.

### Technical skills
Single pipe-separated line. Same format as Core Competencies — pull from `master-cv.md` and reorder per JD.

---

## LENGTH

Match the master's length, then size to the role:
- Early-career or mid-career roles where 1 page is expected → 1 page
- Industries where 1-page is the norm (consulting, finance) → 1 page
- Senior IC / lead / manager / director roles that earn the depth → up to 2 pages

For 1-page tailoring, the priority cuts are:
1. Trim older or less relevant roles to 1-2 bullets each
2. Drop the Selected Applied AI Projects section unless absolutely critical
3. Tighten the professional summary to 3–4 sentences
4. Reduce signature achievements to 3–4 bullets

---

## FILE NAMING

Per global rule (`CLAUDE.md`), all output files use **spaces, not underscores**.

Pattern: `Resume [LastName] - [Company] - [Role] - [YYYY-MM].docx`

Examples:
- `Resume [LastName] - Atlassian - Senior PM - 2026-04.docx`
- `Resume [LastName] - Microsoft - Program Manager Supply Chain - 2026-04.docx`
- `Cover Letter [LastName] - Atlassian - Senior PM - 2026-04.docx`

---

## DOCX GENERATION

When producing a `.docx`, use python-docx and follow `.claude/rules/docx-generation.md` for:
- File naming (spaces, not underscores)
- Visual verification before declaring done
- No table-based layouts that ATS parsers choke on
- Standard fonts
- Single column

The reference template is the master resume. The cleanest path is to **load the master file as a starting point and mutate it** — replace the summary, replace the signature achievements, reorder competencies, modify role bullets — rather than building from scratch. Building from scratch silently breaks visual fidelity (wrong font, wrong margins, missing formatting). Mutating the template in place guarantees the output matches whatever font, margins, and spacing the master uses. See `.claude/rules/docx-generation.md` Rule 8.

---

## COVER LETTER FORMAT

When a cover letter is drafted, follow the user's existing cover letter template when one is provided:

```
[YOUR FULL NAME]
City, ZIP | phone | email | LinkedIn

Dear Hiring Manager,

[Paragraph 1: 2–3 sentences. State the role applied for, years of experience, and core fit claim.]

[Paragraph 2: 4–5 bullets summarizing the most JD-relevant accomplishments from the current role. Use a "Currently, as a [Title] at [Company], I lead..." opener.]
- Bullet 1
- Bullet 2
- Bullet 3
- Bullet 4

[Paragraph 3: 2–3 sentences. Pull a specific past role / accomplishment that maps to a major JD requirement.]

[Paragraph 4: 1–2 sentences. Cultural fit angle — why this specific company.]

[Closing: 2 sentences. Direct close, gratitude, ask for the conversation.]

Sincerely,
[Your Name]
```

**Note:** When the user has an existing cover-letter format, default to it. The Pitch playbook has slightly stronger opener guidance ("don't start with 'I am writing to express my interest'"). When tailoring, default to the user's existing format unless a specific employer / industry calls for a different style. Mention the trade-off in the fit summary if you want to suggest a stronger opener.

Length: keep to one page. ~300–400 words.

---

## CHANGE LOG

- Format reference created from a user's master resume and cover-letter templates, then generalized.
