# Setting Up Your GitHub (the right architecture)

You don't need to be technical to keep your work organized the way professionals do. The idea is simple: instead of one messy folder, you keep a few focused **repositories** (think of each as a labeled, backed-up project folder that lives safely in the cloud and that Claude can read and help with).

You do not need this on day one. Get comfortable with the job kit first. Come back here when you're ready to grow.

---

## The architecture (what goes where)

A clean, useful setup for someone selling their experience looks like this:

| Repository | Private? | What it's for |
|---|---|---|
| **`career`** (this kit) | Private | Your master CV, your story, tailored resumes, cover letters, the jobs you're targeting. Your job-search command center. |
| **`knowledge`** | Private | What you know. Your field expertise, key contacts, a running archive of wins and projects, lessons, notes. Claude reads this to get smarter about you over time. This is your edge. |
| **`projects`** or one repo per venture | Private | Any business, side project, or initiative you're working on, each in its own repo. |

Three rules that keep it clean:

1. **Private by default.** Anything with your real history, contacts, or numbers stays private. Make a repo public only when you deliberately want the world to see it.
2. **One README per repo** — a short note at the top saying what the repo is for, so future-you (and Claude) always know.
3. **Keep personal data out of anything public.** If you ever publish something, it should be the template or the tool, never your filled-in details.

This is the same idea the pros use: separate, focused, private, backed up, and readable by your AI assistant.

---

## The setup prompt (run when you're ready)

Open Claude Code and paste this. It will check that your GitHub is connected, then set up the architecture with you, explaining each step.

```
I want to set up my GitHub the way an organized professional would, and I'm a beginner, so guide me one step at a time in plain English and explain what each thing is as we go.

1. First, check whether I'm signed in to GitHub from the command line (try `gh auth status`). If I'm not, walk me through signing in simply, and if it needs me to do something in a browser, tell me exactly what to click.

2. Then explain, in one or two plain sentences each, what a "repository" is and why keeping a few focused private ones beats one big folder.

3. Help me create these private repositories, and put a short README in each that says what it's for:
   - "knowledge" — for what I know: my expertise, my contacts, my archive of accomplishments, my notes. Explain that Claude will read this to understand me better over time, and help me write the first couple of notes today.
   - (ask me if I have any business or project I want its own repo for, and if so, create it too)

4. Explain how I open any of these in Claude Code later so you can help me with them.

5. Give me one small next step for keeping these up to date without it becoming a chore.

Keep it encouraging and simple. Setting up one private "knowledge" repo with two real notes today is a win.
```

---

The point of all this isn't to be tidy for its own sake. It's that the more your assistant knows about your real experience and your real network, the better it gets at helping you sell yourself. Your knowledge repo is the thing that compounds.
