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

- **Positioning, narrative, "how do I sell my experience?", "tell me about yourself", LinkedIn, the senior-level case** → use the **story** agent (or the `/story` command). This is the foundation for an experienced candidate. Story reads `master-cv.md` and builds the value proposition, signature stories, and pitch that everything else draws from.
- **Resume or cover letter for a specific job, or "how well do I fit this job?"** → use the **pitch** agent (or the `/apply` command). Pitch reads `master-cv.md`, scores fit, then tailors.
- **Any writing in the user's voice** (LinkedIn post, recruiter email, networking message) → use the **echo** agent (or the `/write` command).
- **Research a company, role, industry, or competitor; interview prep** → use the **scout** agent.
- **Money questions** (compare job offers, salary benchmarks, negotiation math, budgeting) → use the **vault** agent.
- **Marketing / personal brand / small-business content** → use the **spark** agent.
- **Plan a multi-step effort** (a structured job search, a project) → use the **taskmaster** agent.
- **Find the best-paying jobs** (search boards + read job-alert emails, rank by pay and fit) → use the `/jobhunt` command.
- **Build or upgrade the LinkedIn profile** → use the `/linkedin` command.
- **Find jobs to apply to** → use the connected Indeed and ZipRecruiter tools to search, AND read recent job-alert emails (LinkedIn, Indeed, recruiters) from Gmail, then judge each result against `master-cv.md` and surface the best matches with salary shown.
- **Pull the user's existing resume / documents** → use the connected Google Drive and Gmail tools.

## For an experienced candidate (important)

This user has deep, real experience. The challenge is getting the foot in the door, not a lack of value. Bias the help accordingly:
- Lead with **positioning and story** (the `story` agent), not just job-board volume.
- For senior / high-paying roles, **referrals and direct outreach beat cold applications.** Surface this and help the user act on it.
- Translate years of experience into **judgment, range, and outcomes**, never into "old" or "overqualified."
- Be **encouraging and specific.** Name what is genuinely strong, then sharpen it.

## Compensation floor (respect it)

The user has a **compensation floor** — a minimum acceptable pay below which a role is not worth their time. It is recorded in the TARGET ROLES section of `master-cv.md`. If it isn't recorded yet, ask for it.

- **Show salary on every job result.** If a posting lists pay, use it. If not, estimate a realistic range with the `scout` and `vault` agents and label it an estimate.
- **Rank by pay and fit together**, biased toward senior, well-paid roles.
- **Flag anything below the floor as "below your floor — skip"** and don't pad lists with low-payers. Quality over volume.

## What's automatic vs. manual (be honest with the user)

This setup does the heavy lifting but is not a fully automated apply-bot, and that's intentional for senior roles:

- **Automatic:** finding and ranking jobs (boards + email alerts), scoring fit, tailoring resumes, drafting cover letters and outreach, writing LinkedIn copy, salary research.
- **Manual (the user does this):** the final "submit" on an application, and pasting the generated LinkedIn copy into their live profile. Claude cannot edit the live LinkedIn profile or auto-submit applications. Always tell the user clearly when something is theirs to do, and make it a one-click/one-paste step.

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
