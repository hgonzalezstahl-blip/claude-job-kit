# One-Time Setup

Copy **everything inside the code block below** and paste it as your first message to Claude Code (with this `claude-job-kit` folder open). Then just answer Claude's questions. You only do this once.

---

```
You are helping me set up my personal job-application workspace. I'm new to Claude Code, so go slowly, explain things in plain English, and ask me one thing at a time. Don't dump a wall of questions on me.

First, read these files so you understand how this workspace works:
- CLAUDE.md (in this folder)
- .claude/agents/pitch/master-cv.md
- .claude/agents/pitch/resume-playbook.md
- .claude/agents/echo/style-profile.md

Here is the plan. Walk me through it step by step:

STEP 1 — Find what I already have.
Ask me if I have an existing resume. If I do, offer to pull it from my Google Drive or my Gmail (search my connected accounts), or let me paste it in or drop the file in this folder. Read whatever I give you. If I don't have one, that's fine, we'll build it from scratch through conversation.

STEP 2 — Build my master CV.
Fill in .claude/agents/pitch/master-cv.md with my real career history. This is the most important step, because every resume you ever make for me draws only from this file. Go section by section (identity, then each job, then education, then skills, then projects). For each job, ask me what I actually did and dig for numbers: how many people, how much money, how much time saved, what scale. If I'm vague, ask follow-up questions to get something concrete, but never invent a number. Save my answers into the file as we go. Don't try to do all of it in one shot. It's okay if this takes a while.

STEP 3 — Define what I'm aiming for.
Help me get clear on what jobs I should target. Ask me about my experience, what I liked and didn't like, where I want to work (city, remote, hybrid), and what level I'm at. Then suggest 2 or 3 specific role titles I'm a realistic fit for, and explain why. Write these into the TARGET ROLES section of my master CV.

STEP 4 — (Optional) Capture my writing voice.
Ask if I want cover letters and messages written to sound like me instead of like generic AI. If yes, ask me to paste 2 or 3 things I've written (an email, a note, anything), and save them into .claude/agents/echo/style-profile.md. If I don't care about this right now, skip it.

STEP 5 — Show me how to actually use this.
Once my master CV has real content, explain in plain English how I do the everyday stuff:
- How to find jobs: tell me I can ask you to search Indeed and ZipRecruiter for my target roles near my location, and you'll rank them against my background.
- How to apply: tell me to type /apply and paste a job description, and you'll score my fit first, then tailor a resume.
- How to write something in my voice: tell me to type /write and say what I need.

STEP 6 — Do a real first run.
Offer to search Indeed and ZipRecruiter right now for my target roles, show me the 5 best matches with a one-line reason for each, and ask if I want to /apply to any of them.

Start with Step 1. Keep it friendly and simple.
```

---

## After setup

You're done with this file. From now on you just use:

- **`/apply`** then paste a job → tailored resume
- **`/write`** then say what you need → writing in your voice
- Or ask Claude in plain English to **search for jobs** or **find your old documents**

If you ever want to add a new accomplishment or job to your history, just tell Claude "add this to my master CV" and describe it.
