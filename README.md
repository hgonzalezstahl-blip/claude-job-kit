# Claude Job Kit

A personal job-application workspace for Claude Code. This one folder holds everything: your career history, two AI assistants that tailor resumes and write in your voice, the job descriptions you're targeting, and the resumes and cover letters they produce.

You don't need to understand any of the files. You talk to Claude in plain English and it does the work.

---

## What's inside

| Assistant | What it does | How you call it |
|---|---|---|
| **Story** | Turns your experience into a clear, compelling story so people see your value fast. Your value proposition, signature stories, "tell me about yourself," LinkedIn, and the case for a senior role. **Start here.** | Type `/story` |
| **Pitch** | Reads a job description, scores how well you fit, then tailors your resume (and a cover letter if you want one) to that specific job. Never makes anything up. | Type `/apply` and paste a job description |
| **Echo** | Writes things in *your* voice, not generic AI voice. Cover letters, LinkedIn posts, recruiter emails. | Type `/write` and say what you need |
| **Job hunt** | Searches the boards *and* reads the job-alert emails sent to your Gmail, ranks by pay and fit, and skips anything below your salary floor. | Type `/jobhunt` |
| **LinkedIn** | Writes your full profile (headline, About, experience, skills) ready to paste in. | Type `/linkedin` |
| **Scout** | Researches a company, role, or industry before you apply or interview. Interview prep. | Just ask: "research [company] for my interview" |
| **Vault** | Money questions: compare two job offers, salary benchmarks, negotiation math, budgeting. | Just ask: "compare these two offers" |
| **Spark** | Marketing and personal-brand content if you want it. | Just ask |
| **TaskMaster** | Lays out a step-by-step plan (e.g. a 4-week job search). | Just ask: "plan my job search" |

Everything these assistants know about you comes from two files you fill in once:

- `.claude/agents/pitch/master-cv.md` — your complete career history (every job, project, number). This is the single source of truth.
- `.claude/agents/echo/style-profile.md` — samples of your writing, so Echo can sound like you. (Optional — only needed if you want cover letters or posts in your voice.)

---

## Folder map

```
claude-job-kit/
  README.md          <- you are here
  SETUP.md           <- the one-time setup prompt (open this next)
  CHEATSHEET.md      <- one-page quick reference
  CLAUDE.md          <- instructions Claude reads automatically
  tracker.md         <- log of what you've applied to
  jobs/              <- save job descriptions here
  resumes/           <- tailored resumes land here
  cover-letters/     <- cover letters land here
  GITHUB-SETUP.md    <- (later) organize your GitHub the pro way
  BUILD-YOUR-OWN.md  <- (later) start building your own assistants
  .claude/           <- the AI assistants live here (don't edit)
```

---

## First-time setup (about 30 minutes, once)

1. **Install Claude Code** if you haven't: https://claude.com/claude-code — then sign in.
2. **Open this folder in Claude Code.** On Windows, open a terminal in this folder and type `claude`, or open the folder in the Claude desktop/VS Code app.
3. **Open `SETUP.md`, copy the whole prompt inside it, and paste it into Claude.** Claude will interview you, pull in your existing resume if you have one in Google Drive or email, and fill out your master CV with you. Just answer its questions.
4. That's it. After setup you're ready to apply.

---

## Everyday use

**To apply to a job:**

```
/apply
```
Then paste the job description (or a link). Pitch gives you a fit score first, asks if you want to proceed, then produces a tailored resume in the `resumes/` folder.

**To write a cover letter or a message in your voice:**

```
/write a cover letter for the job in jobs/acme-analyst.md
```
or
```
/write a short LinkedIn message to a recruiter at Acme about the analyst role
```

**To find jobs to apply to**, just ask Claude in plain English, e.g.:

> Search Indeed and ZipRecruiter for [your target role] jobs near [your city] posted in the last week, and show me the 10 best matches for my background.

Claude uses your connected Indeed and ZipRecruiter accounts to search, and your master CV to judge fit.

---

## The one rule that matters

Pitch and Echo will **never invent** a job, a number, a title, or an accomplishment. Everything on your resume traces back to something real in your master CV. If a job asks for something you don't have, they tell you honestly instead of faking it. That keeps you safe in interviews.
