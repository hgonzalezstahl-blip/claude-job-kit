---
description: Find the best-paying jobs that fit your experience, from job boards and your email alerts
allowed-tools: Agent, Read, WebFetch, WebSearch
---

Find and rank the best jobs for me. Aim high: I have deep experience and I'm targeting senior, well-paid roles. Steps:

1. Read `.claude/agents/pitch/master-cv.md` for my experience, my target roles, and my **compensation floor** (my stated minimum acceptable pay). If no floor is recorded yet, ask me for it before searching.

2. Search Indeed and ZipRecruiter for my target roles, near my location and remote, biased toward senior titles (Manager, Director, Principal, Lead, Senior) and higher pay bands.

3. Also check my Gmail for recent job-alert emails (LinkedIn, Indeed, ZipRecruiter, recruiters) and pull those roles in too.

4. For each role, show me a clean row: title, company, location, **salary** (use the posted figure; if none is listed, estimate a realistic range using the `scout` and `vault` agents and label it an estimate), and a one-line reason it fits my background.

5. Rank by pay and fit together. Anything below my compensation floor: flag it as "below your floor — skip" and do not pad the list with low-payers. I would rather see 5 strong, well-paid matches than 30 mediocre ones.

6. Ask which roles I want to pursue. For each one I pick, hand off to the `pitch` agent (the same as `/apply`) to produce a tailored resume, and offer a cover letter and a referral/outreach message in my voice.

**Optional focus (leave blank to search all my target roles):**

$ARGUMENTS
