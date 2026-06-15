---
name: section-expansion
description: Decide which resume sections to include, expand, compress, or omit for a specific job application. Use whenever Pitch tailors a resume or LinkedIn-facing profile strategy: work authorization/citizenship, selected projects, certifications, education, role depth, skills/competencies, languages, portfolio attachments, and LinkedIn consistency. Reads master-cv.md as source of truth and never hard-codes personal project lists into the skill.
---

# Section Expansion

Use this skill to decide what belongs on one tailored resume. Keep facts in the source file: read `.claude/agents/pitch/master-cv.md`, optional portfolio docs, and the job description. This skill provides the decision method, not the user's personal inventory.

## Inputs

Read:

1. Target job description.
2. `master-cv.md`.
3. Existing target resume constraints, if any: one page, two page, executive bio, LinkedIn, portfolio.
4. Project/portfolio source files only when the JD rewards project evidence.

If the source is missing or placeholder-only, stop and ask the user to populate it.

## Core Rule

The tailored resume is a sourced subset of the master CV. Never add a section, project, skill, credential, or metric unless it is sourced in `master-cv.md` or explicitly confirmed in the current conversation.

## Section Decisions

### Work Authorization / Citizenship

Default: omit from resume.

Include only when the JD requires citizenship, clearance, work authorization, export-control eligibility, or a regulated role where the requirement is a hard screen. Place it low on the resume or in an "Additional" line unless the JD makes it central.

### Selected Projects / Portfolio

Include project sections when the JD rewards builder evidence: AI, automation, product, technical transformation, consulting, innovation, systems implementation, or portfolio-backed roles.

Before listing any project, classify it:

| Project type | Resume placement |
|---|---|
| Employer-built or employer-context work | Under the relevant role, not as a personal project |
| Independent / personal / open-source work | Selected Projects or portfolio section |
| Confidential / private / not sanctioned for public reference | Omit or describe only at a safe abstraction level |
| Weak or outdated project | Keep out unless the JD specifically asks for it |

Use the master CV to choose the top 2-3 projects. Do not rely on a fixed default lineup.

### Certifications

Promote certifications when the JD names them, the role family strongly values them, or the credential differentiates the user for that application. Otherwise keep them in education/additional credentials.

### Education

Keep education concise by default. Expand coursework, research, honors, or thesis/project work only when the JD explicitly values the degree program, academic domain, policy/research angle, or recent coursework.

### Professional Experience Depth

Expand the most relevant roles. Compress older or less relevant roles.

Guidelines:

- Most recent or most relevant role usually gets the most bullets.
- A directly relevant older role may expand while a less relevant recent role stays concise.
- For one-page resumes, cut older detail before cutting the strongest evidence.
- Do not trim below the point where the career story becomes incoherent.

### Skills / Core Competencies

Use 10-15 high-signal skills. Reorder so the JD's must-have language appears early, but only when the master CV supports it.

Classify each JD keyword:

| Classification | Action |
|---|---|
| Have it and named | Use exact JD language if accurate |
| Have it but named differently | Translate honestly into JD language |
| Adjacent | Use sparingly and explain through experience bullets |
| Genuine gap | Do not add; flag in the fit diagnostic |

### Languages

Surface languages when the JD, geography, customer base, or stakeholder environment makes them useful. Otherwise keep them in skills or omit.

### Portfolio Attachments

Attach or reference portfolios only when the recruiter asks, the application portal supports multiple attachments, or a direct hiring-manager conversation rewards depth. Do not auto-attach extra documents to every cold application.

### LinkedIn Consistency

The resume can be narrower than LinkedIn, but it cannot contradict LinkedIn.

- Same companies, titles, dates, and education.
- Resume gets the most specific JD-relevant evidence.
- LinkedIn stays broad enough to support all target role families.
- Avoid exact public metrics on LinkedIn if private resumes may frame them differently.

## Output

```text
SECTION PLAN: [Company] - [Role]

Include / Expand:
- [section] - [why, with master-cv source area]

Compress / Omit:
- [section] - [why]

Keywords to surface:
- [keyword] - [source / classification]

Risks:
- [fabrication, confidentiality, sanction, or fit risk]

Portfolio / LinkedIn notes:
- [action or none]
```

## Rules

1. The skill provides decision logic only. Personal inventories stay in the source file.
2. Never imply employer-owned work is an independent personal project.
3. Never list private, confidential, or unsanctioned work as public portfolio proof.
4. Every included claim must survive `no-fabrication`.
