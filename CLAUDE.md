# Project Instructions — Claude Job Kit

This folder is a personal job-application workspace. Read this before doing anything in it.

## What lives where

- `.claude/agents/pitch/master-cv.md` — the user's complete career history. **Single source of truth.** Every claim on any resume must trace to a line in this file.
- `.claude/agents/echo/style-profile.md` — the user's writing-voice samples (for Echo).
- `jobs/` — saved job descriptions (one file per job).
- `resumes/` — tailored resume outputs.
- `cover-letters/` — cover letter outputs.
- `tracker.md` — running log of applications.

## Routing — which assistant to use

- **Resume or cover letter for a specific job, or "how well do I fit this job?"** → use the **pitch** agent (or the `/apply` command). Pitch reads `master-cv.md`, scores fit, then tailors.
- **Any other writing in the user's voice** (LinkedIn post, recruiter email, message) → use the **echo** agent (or the `/write` command).
- **Find jobs to apply to** → use the connected Indeed and ZipRecruiter tools to search, then judge each result against `master-cv.md` and surface the best matches.
- **Pull the user's existing resume / documents** → use the connected Google Drive and Gmail tools.

## Hard rules (never break)

1. **Never fabricate.** No invented jobs, titles, dates, numbers, certifications, or accomplishments. If `master-cv.md` doesn't support a claim, don't make it. Flag genuine gaps honestly. This protects the user in interviews.
2. **No em dashes and no ALL-CAPS-for-emphasis in any prose written for a human reader** (cover letters, posts, emails). Use periods, commas, semicolons, colons, or parentheses. This is the clearest AI tell.
3. **File names use spaces, not underscores.** Example: `Resume Gonzalez - Acme - Analyst - 2026-06.docx`, not `Resume_Gonzalez...`.
4. **One resume per job.** Never reuse a tailored resume across applications. Re-tailor every time.
5. **Resumes are ATS-safe:** single column, standard section headings, standard fonts, `.docx`. No tables, text boxes, graphics, or skill-rating bars.
6. If `master-cv.md` still has placeholder/bracketed content, say so and help the user populate it before drafting anything.

## Dates

Use the real current date for filenames and "applied on" entries. Ask or check the system date; don't guess a year.

## After an application

Append a row to `tracker.md` (company, role, date applied, fit score, status, link).
