---
description: Build tailored resume + cover + fit diagnostic for SEVERAL jobs at once (in parallel), then quality-check them all
allowed-tools: Agent, Read, Bash
---

Build application packages for multiple roles in one pass. Use this after `/jobhunt` surfaces several good roles, or when the user pastes a list of jobs. Keep it calm and in plain English; if the user is non-technical, build 3-5 at a time, not 30.

1. **Collect the target roles.** From `$ARGUMENTS` (a list of jobs or JD files), or ask the user which of the recent `/jobhunt` results (or rows in `tracker.md`) to build. Confirm the short list back in one line before building.
2. **Build them in parallel.** For EACH role, spawn a **pitch** subagent (send them in one message so they run at once) that follows the `/apply` workflow: read `.claude/agents/pitch/master-cv.md` + `.claude/agents/pitch/resume-playbook.md`, produce the JD Fit Diagnostic, then the tailored resume `.docx` + cover letter `.docx` into a per-role folder in Downloads. Every agent must obey the docx-generation rules: template mutation (RULE 8), spacing audit (RULE 9), **bold discipline (RULE 10 — never bold a whole bullet)**, no em dashes, font match, and no fabrication.
3. **Quality-check everything once.** After all agents finish, run `py tools/verify_docx.py "<the Downloads batch folder>"` over the whole batch. For any file flagged OVER-BOLD, run `py tools/fix_bold.py "<that resume>"`; fix any em-dashes or placeholders it flags. Re-run verify until it reports **All clean**.
4. **Report.** A short table: role | fit score | files | anything fixed. Then remind the user, plainly, that clicking submit on each application is theirs to do.

$ARGUMENTS
