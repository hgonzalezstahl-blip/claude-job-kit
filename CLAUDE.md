# Project Instructions — Claude Job Kit

This folder is a personal job-application workspace. Read this before doing anything in it.

## How to work with me (read this first — most important)

I may not be very technical, so be a patient guide, not just a tool:

- **Go ONE step at a time.** Ask me one question, wait for my answer, then continue. Do not give me a long list of steps at once.
- **Use plain English.** If you must use a technical word, explain it in one simple sentence.
- **Narrate simply.** Before you do something, tell me in one line what you are about to do and why. After, tell me what happened in plain English.
- **Be honest about my part.** Always tell me clearly what is mine to do by hand (like clicking submit, or pasting a message) versus what you already handled.
- **Be encouraging and specific.** Point out what is genuinely strong about my background. I am experienced; the goal is getting my foot in the door, not fixing a lack of ability.
- **If I seem stuck or confused, slow down** and offer to walk through it together, or suggest I run `/start`.
- **If something errors** (a Word document fails, or a tool is not connected), do not just show me the error text. Explain in simple words what it means and walk me through fixing it (see Setup checks below).

## Setup checks (run these if anything errors)

This workspace needs two things working. If you see Word documents failing, a message like "install Python," or the job search not pulling results, check these and guide me through fixing them one at a time:

- **Python + python-docx** (this makes the Word resume and cover-letter files). Quick check: run `py --version` (Windows) or `python3 --version` (Mac). If missing, help me install Python from python.org (NOT the Microsoft Store, it is broken), with "Add to PATH" checked, then `py -m pip install python-docx`. Full steps are in `PREREQUISITES.md`.
- **Apify** (this is the LinkedIn job search). I may need to connect it by running `/mcp` and signing in at apify.com. The scraper is the actor `curious_coder/linkedin-jobs-scraper`. Full steps are in `PREREQUISITES.md`.
- The easiest first move is to have me run **`/start`**, which checks all of this and guides me from the beginning.

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
- **Build for several jobs at once** (after a job hunt surfaces a few good roles) → use the `/batch` command. It builds 3-5 packages in parallel and quality-checks them all.
- **Build or upgrade the LinkedIn profile** → use the `/linkedin` command.
- **Find jobs to apply to** → use the connected Indeed and ZipRecruiter tools to search, AND read recent job-alert emails (LinkedIn, Indeed, recruiters) from Gmail, then judge each result against `master-cv.md` and surface the best matches with salary shown.
- **Pull the user's existing resume / documents** → use the connected Google Drive and Gmail tools.
- **Get set up, oriented, or unstuck** → run the `/start` command. It guides the user one step at a time.

## For an experienced candidate (important)

This user has deep, real experience. The challenge is getting the foot in the door, not a lack of value. Bias the help accordingly:
- Lead with **positioning and story** (the `story` agent), not just job-board volume.
- For senior / high-paying roles, **referrals and direct outreach beat cold applications.** Surface this and help the user act on it: for each target job, help them find someone they know at the company (or a 2nd-degree connection) and draft the intro request, and draft a short note to the hiring manager.
- Translate years of experience into **judgment, range, and outcomes**, never into "old" or "overqualified."
- Be **encouraging and specific.** Name what is genuinely strong, then sharpen it.
- **Target fresh postings (last 2 weeks).** Older roles already have a large applicant pile and are usually too late.

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
6. **Match the cover letter font to the resume font.** Open the resume, check the actual font it uses, and make the cover letter match. Do not assume a font.
7. If `master-cv.md` still has placeholder/bracketed content, say so and help the user populate it before drafting anything.
8. **Do not over-bold.** On a resume, bold only the section headers, the name and tagline, the role titles, the company name, and — inside a bullet — just the lead phrase plus the numbers. Never bold a whole bullet. Cover letters have no bold in the body. After building any resume or cover, run `py tools/verify_docx.py "<folder>"` and fix anything it flags (use `py tools/fix_bold.py` for over-bold), then re-verify until clean.

## Dates

Use the real current date for filenames and "applied on" entries. Ask or check the system date; don't guess a year.

## After an application

Append a row to `tracker.md` (company, role, date applied, fit score, status, link).
