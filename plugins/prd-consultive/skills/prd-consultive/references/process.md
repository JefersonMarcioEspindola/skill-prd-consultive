# Consultative process

Each phase has a goal and an exit criterion. Don't move on until the criterion is met, and don't linger in a phase once it is: the board exists to settle doubts, not to drag the conversation out.

Everything here is in English for convenience. In the session, use the user's language for every line, table and label (see SKILL.md, section 1).

## Contents

- Phase 0: Triage
- Phase 1: Understanding
- Phase 2: Board, round 1
- Phase 3: Rebuttals
- Phase 4: Convergence
- Phase 5: Verdict and gate
- Phase 6: Generation
- Pace control
- `idea.md` format

---

## Phase 0: Triage

**Goal:** know what's on the table and how deep to go.

1. If the user hasn't told the idea yet, ask for it in one or two sentences. Don't ask for more than that now.
2. Identify the **document type**, because it changes who sits on the board:

| Type | Example | Board |
|---|---|---|
| New product | "an app for personal trainers to manage clients" | Helena, Caio and Bia, plus Lúcia if there's a trigger |
| Feature in an existing product | "add recurring payments to my SaaS" | Helena talks about business impact instead of market; Caio and Bia as usual |
| Technical or refactor | "migrate the backend from Express to Nest" | Caio leads; Helena talks about cost and risk; Bia only joins if the end user feels the change |

3. Confirm the mode (see SKILL.md) and, if you have file access, create `idea.md`. As soon as you know the audience, choose who plays the ideal customer, Bia or Lucas (rule in `references/board.md`). Wherever this file says "Bia", read "the chosen ideal customer".
4. Say in one line how it works and that the user controls the pace: "First I understand the idea, then the board challenges it, and I only write the PRD when no doubt is left. If you want to speed up at any point, just say so."

**Exits when:** type and mode are set.

## Phase 1: Understanding

**Goal:** understand the idea well enough for the board to challenge something concrete, not a cloud.

Use blocks 1 to 3 of `references/interview.md` (problem, audience, solution and current alternative). One or two rounds are usually enough. Téo leads here, in a neutral tone; the personas don't give opinions yet.

Build and show the **positioning statement**:

> For **[audience]** who **[pain]**, **[product]** is **[category]** that **[main benefit]**. Unlike **[current alternative]**, **[differentiator]**.

Ask the user to confirm or correct it. If they can't fill in a bracket, that's already material for the board, not a reason to stall: mark the bracket as "open for the board".

**Exits when:** the statement is confirmed (even with brackets marked as open).

## Phase 2: Board, round 1

**Goal:** surface the strongest objections early, while changing course is still cheap.

1. Téo opens in one or two lines: who's on the board and how it will work.
2. Each persona speaks once, in the format from `references/board.md`: signal, short take, main objection and one question. Order: Helena, Caio, Bia and, if there's a trigger, Lúcia.
3. Téo closes with the **objection board** and the consolidated questions: at most 4, prioritized by how much they change the product, each with options when possible.

Objection board (show as a table and update every round):

| # | Objection | Raised by | State |
|---|---|---|---|
| O1 | A free spreadsheet already solves it for most people | Helena | open |
| O2 | The official WhatsApp API depends on Meta's approval, outside our control | Caio | open |

Possible states: `open`, `decided`, `scope changed`, `accepted risk`.

**Exits when:** every persona has spoken and the questions have been asked.

## Phase 3: Rebuttals

**Goal:** close the objection board.

1. The user answers.
2. Only those with something new to say about what changed react. A persona who hasn't changed her mind doesn't repeat the argument; at most she says in one line that she keeps her signal and why.
3. A persona changes signal when she gets an argument or a fact that knocks down her objection, never because the user insisted or showed excitement. When she changes, she says what convinced her.
4. Téo updates the board.
5. Repeat until no objection is `open`, or up to 3 rounds. After the third, Téo proposes a destination for what's left ("make it an accepted risk?", "cut it from the MVP?") and the user chooses.

**Exits when:** no objection is `open`.

## Phase 4: Convergence

**Goal:** turn the validated idea into something buildable. Use blocks 4 to 7 of `references/interview.md` and `references/stack.md`.

Each topic has an owning persona, so the conversation doesn't become an ownerless interrogation:

| Topic | Who leads | What has to come out |
|---|---|---|
| MVP scope | Caio, with Bia | List of what's in and what's out, with the reason for each cut |
| Main flows | Bia | 2 to 4 flows, step by step, from the user's point of view |
| Data | Caio | Main entities and how they relate |
| Stack | Caio | Decisions with the why (see `references/stack.md`) |
| Success metric | Helena | 1 main metric and 2 or 3 supporting ones, with target and deadline |
| Regulatory risks | Lúcia, if she's on the board | What's mandatory from day 1 |

Propose instead of asking whenever you can. "From what you said, the MVP has A, B and C, and D waits because X. Right?" is much faster than "what's in the MVP?".

**Exits when:** the six items in the table are defined (the last one only when Lúcia takes part).

## Phase 5: Verdict and gate

**Goal:** close with clarity and only write the document with the user's approval.

1. **Verdict:** each persona gives the final signal and one sentence. If the environment allows visuals in the chat, this is one of the two moments to use them (board cards).
2. **Two or more reds:** Téo says so clearly, sums up the reasons and offers two or three paths (pivot the audience, reduce scope, validate hypothesis X before building). The decision is the user's. If they want to go ahead anyway, go ahead, and the board's opinion goes into the PRD as it was given, without softening.
3. **Decision sheet** (the other moment for visuals in the chat):

```markdown
## Decision sheet: <product>

**Positioning:** <phase 1 statement, final>
**Type:** <new product | feature | technical>

**Board verdict:** Helena 🟢 · Caio 🟡 · Bia 🟢 <· Lúcia, if she took part>

**MVP includes:** <items>
**Left out:** <items, with a short reason>
**Stack:** <decisions>
**Main metric:** <metric, target, deadline>

**Decisions made:** <D1, D2...>
**Accepted risks:** <R1, R2...>
**Assumptions (confirm or correct):** <what was inferred without confirmation>

Can I write the PRD? Do you also want PLAN.md with the tasks?
```

4. Wait for an explicit yes. A correction to the sheet is not a yes: apply it, show only what changed and ask again.

**Exits when:** the user approves the sheet.

## Phase 6: Generation

Follow section 8 of SKILL.md. The PRD contains nothing that isn't in the sheet or in `idea.md`. If, while writing, you notice a gap, stop and ask a single short question instead of making something up.

---

## Pace control

The user sets the pace. Recognize these requests, in any wording or language:

- **"Speed up" / "skip" / "enough board":** Téo sums up the board, proposes a destination for each open objection (usually accepted risk or a scope cut) and goes straight to convergence or the gate. Objections don't vanish: they become accepted risks, and the user confirms that in the sheet.
- **"Go back" / "I changed my mind about X":** go back only as far as needed, update the board and `idea.md`, and say what changed.
- **"I only want to hear Helena" (or another persona):** do it. The board serves the user.
- **Short answers or impatience:** drop to 2 questions per round and propose more than you ask.

## `idea.md` format

A working file, not a presentation. Update it at the end of each phase. When the conversation resumes after a context summary, read this file before continuing. Write it in the session's language.

```markdown
# <product>: board log

Mode: <fast | consultative> · Type: <new product | feature | technical> · Current phase: <n> · Language: <language> · Country: <country>

## Positioning
<statement>

## User answers
- <block>: <summary of the answer>

## Objection board
| # | Objection | Who | State | How it was resolved |

## Decisions
- D1: <decision> (because <reason>; rejected alternative: <x>)

## Accepted risks
- R1: <risk> (raised by <persona>; mitigation: <x>; revisit when: <trigger>)

## Assumptions
- <what was inferred without confirmation>

## Signals
Helena: <signal> · Caio: <signal> · Bia: <signal> · Lúcia: <signal or "didn't take part">
```
