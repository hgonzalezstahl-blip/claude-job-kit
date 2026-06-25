---
description: Invoke Pitch to produce a JD Fit Diagnostic + tailored resume (and optional cover letter) for a specific job
allowed-tools: Agent, Read
---

Spawn the **pitch** subagent to produce application materials for the job described below. Pitch must:

1. Read `.claude/agents/pitch/master-cv.md` first.
2. Read `.claude/agents/pitch/resume-playbook.md` second.
3. If the master CV has placeholder content, refuse and ask the user to populate it.
4. Parse the job description in `$ARGUMENTS` (or `job-target.md` if `$ARGUMENTS` is empty).
5. Map JD requirements to the user's actual experience.
6. **Produce the JD Fit Diagnostic FIRST** (Step 2.5 in Pitch's workflow): match score out of 100, top 5 missing keywords with honest classification, 3 red flags a hiring manager would spot, ATS scan, stop-the-scroll check. Save as `Fit Diagnostic - [Company] - [Role].md` in Downloads.
7. **Ask the user if they want to proceed** with the tailored resume. If match score is below 70, explicitly flag and suggest pursuing a warm intro before a cold application.
8. If the user proceeds: Draft → keyword audit → corporate-speak scrub → ATS check → template mutation → deliver tailored resume as `.docx` in Downloads.
9. If the user asked for a cover letter, generate it as a separate `.docx` in Downloads.
10. **Quality-check before declaring done.** Run `py tools/verify_docx.py "<the Downloads folder with the new files>"`. If it reports OVER-BOLD bullets, run `py tools/fix_bold.py "<the resume file>"` and re-verify; if it flags em-dashes or leftover placeholders, fix them and re-verify. Only call it done when verify reports **All clean**.
11. Output a fit summary at the end listing strong matches, partial matches, and stretches.

**Job description / target role from the user:**

$ARGUMENTS
