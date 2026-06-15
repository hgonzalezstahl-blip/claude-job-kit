# Claude Job Kit — One-Page Cheat Sheet

Keep this nearby. Everything you do happens by talking to Claude in plain English inside this folder.

---

## The only 3 things you do

**1. Find jobs**
> Search Indeed and ZipRecruiter for [my target role] near [my city] posted this week, and rank the top 10 for my background.

**2. Apply to a job** — type this, then paste the job posting:
```
/apply
```
Claude scores how well you fit *first*, asks if you want to continue, then puts a tailored resume in the `resumes/` folder.

**3. Write something in your voice** — a cover letter, a note to a recruiter, a LinkedIn post:
```
/write a cover letter for the job in jobs/[filename].md
```

---

## Useful plain-English asks

- "Add this to my master CV: ..." — to record a new job, project, or accomplishment.
- "Pull my latest resume from Google Drive and update my master CV."
- "What roles am I a realistic fit for?"
- "Show me what I've applied to." (reads `tracker.md`)
- "Rewrite this to sound less like AI." (paste any text)

---

## When you're stuck

- **You don't know what to type** → just describe what you want in normal words. Claude figures out the command.
- **Claude says your master CV is empty** → it needs your history first. Say "help me fill in my master CV" and answer its questions.
- **A resume looks wrong / made something up** → tell Claude exactly what's off. It will fix it and re-check against your real history. It is built to never invent facts, so flag anything that isn't true.
- **You want to start over on a job** → "redo the resume for [company], this time emphasize [X]."

---

## The promise

Nothing on your resume is invented. Every line traces back to something real you told Claude. If a job wants something you don't have, Claude tells you honestly instead of faking it. That's what keeps you safe and confident in the interview.
