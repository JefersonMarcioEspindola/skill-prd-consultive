# PLAN.md template

The plan turns the PRD into executable work, in pieces a coding agent (or a person) can pick up one at a time. Each task has to be small enough to fit in one session and clear enough to say when it's done. Write it in the session's language; keep the IDs (T-01, FR-01) as they are.

## Rules

- **Dependency order:** a task only comes after what it uses. The foundation (project, database, auth) comes before features.
- **Every phase ends with something you can see working.** Avoid "infrastructure only" phases with nothing to test.
- **Every task references the PRD's FRs** and has a done criterion. A task without an FR has to justify why it exists (setup, deploy).
- **Size:** 3 to 8 tasks per phase. Each task fits in one agent session (ask, build and test in up to 1 or 2 hours); if it looks bigger, split it. A whole MVP usually takes one to three days of work with an agent. Never estimate code in weeks.
- **External dependencies first:** whatever depends on third parties (opening a payment provider account, requesting API access, buying a domain, submitting an app for review) becomes task `T-00` of Phase 1, marked "in parallel", because it runs while the code is written and is usually what sets the launch date.
- **Same sequence as section 14 of the PRD.** If they diverge, one of them is wrong: fix it.

## Structure

```markdown
# <Product>: development plan

> Based on PRD.md v<version>. Stack: <one-line summary>.

## How to use this plan
Run one phase at a time. When each task is done, mark [x] and check the done criteria. Don't start a phase before the previous one works.

## Phase 1: <name> · delivers: <what you can see working at the end>

### T-01. <task name>
- **Requirements:** FR-01, FR-02
- **Depends on:** none
- **What to do:** <2 to 4 objective lines>
- **Done when:**
  - [ ] <verifiable criterion>
  - [ ] <test or manual check>

### T-02. ...

## Phase 2: ...

## Handoff prompt

Paste into your coding agent (Claude Code, Codex, Cursor etc.) inside the project folder:

> Read `docs/PRD.md` and `docs/PLAN.md` before anything else. The PRD is the source of truth: respect section 5 (what's out of the MVP) and section 11 (decisions, with the why of each) and don't change any of that without asking me. Run only Phase 1 of the plan, one task at a time, in order. When each task is done, check the "Done when" criteria, mark the task in PLAN.md and tell me in two lines what was done. If you find something the PRD doesn't answer, stop and ask instead of deciding on your own.
```

Translate the handoff prompt into the session's language too. When delivering, suggest copying `PRD.md` and `PLAN.md` into the project's `docs/` folder, which is where the handoff prompt looks.
