---
name: prd-consultive
description: >
  Writes PRDs the consultative way: before any document, a board of personas (investor, senior dev, ideal customer, moderator and, when the topic calls for it, a legal expert) challenges the idea in the chat until no doubt is left. Then it writes PRD.md (ready for coding agents), PRD.html with the board's verdict and, on request, PLAN.md with tasks. Has a fast mode for ideas already validated. Use it WHENEVER the user wants to create or structure a PRD, spec, product or feature document; validate an app or SaaS idea before building; hear an investor or a developer on an idea; or turn a loose idea into a plan for Claude Code, Codex, Cursor or another agent, even without saying "PRD". Works in any language: use it too for "criar um PRD", "validar minha ideia", "crear un PRD", "validar mi idea".
---

# PRD Consultive

This skill works in any assistant that reads skills in the `SKILL.md` format: Claude (claude.ai and Claude Code), ChatGPT, Gemini and coding agents. It doesn't depend on any specific tool. When the environment offers more (clickable questions, files, code execution, visuals in the chat), use it; when it doesn't, the text-only path works just as well.

A good PRD is an idea that has already been challenged. Coding agents don't ask when a document is vague: they fill the gap with a plausible guess and build on top of it with full confidence. So this skill flips the usual order: **doubts are settled in the chat, up front**, and the final document records decisions, not questions.

The path is always the same, only the depth changes:

```
idea → understanding → board challenges → convergence → gate (decision sheet) → PRD.md → PRD.html (+ PLAN.md)
```

## 1. Language

**Speak the user's language.** The language of the user's first message sets the language of the whole session: the conversation, the personas' lines, the questions, the decision sheet and every document (PRD.md, PRD.html, PLAN.md, idea.md). These instructions are in English only for convenience; never let English leak into a session in another language. Translate every heading, label, signal name and template text. File names stay as they are (`PRD.md`, `PRD.html`, `PLAN.md`, `idea.md`).

The profile can fix a language; if it does, that wins. If the user switches language mid-session, follow them from that point on.

**Country:** infer it from the conversation (language, currency, laws or places mentioned). It changes the local references the board uses: data protection law (LGPD, GDPR, CCPA...), payment methods and currency. If the country matters for a decision (legal, payments) and is still unclear, ask once.

## 2. Read the profile

Before any question, look for the profile in this order and use the first one found:

1. Preferences the user already gave in this conversation or that are in the assistant's memory.
2. `~/.claude/prd-consultive/profile.md` or `~/.agents/prd-consultive/profile.md`, if you can access the computer's files (they live outside the skill folder, so they survive updates).
3. `profile.md` in this skill's folder (the template that ships with it).

If the user wants to set up the profile: with file access, copy the template to one of the paths in item 2 and edit it there. In chat apps (claude.ai, ChatGPT, Gemini), ask for the preferences in one short round and suggest saving them in the app's memory or custom instructions; whoever prefers can edit `profile.md` before uploading the skill. The profile holds the user's preferences: name, language, country, preferred stack, visual theme, brand colors, tone and output folder. Empty fields use the defaults described in the file itself. Don't ask anything the profile already answers: whoever filled it in did so precisely to stop being asked.

## 3. Choose the mode

| | Fast mode | Consultative mode (board) |
|---|---|---|
| For | Already researched, convinced, just wants the document | Has an idea, doesn't know yet if it holds up |
| What happens | One round of gaps, lightning opinion from the board, gate, generation | Understanding, full board with rebuttals, convergence, gate, generation |
| Typical length | 2 to 4 exchanges | 8 to 15 exchanges |

If the user already said the mode, follow it. If not, look at what they brought: rich material (problem, audience, scope and some idea of stack) suggests fast; a one- or two-sentence idea suggests consultative. Ask once, with both options and your recommendation marked, and move on. To avoid spending a whole message on this, ask it together with the first round of questions about the idea: the answers serve both modes.

The user can switch modes at any time ("speed up", "I want the full board"). Respect it and say in one line what changes.

## 4. Rules for both modes

1. **No doubt reaches the document.** Every open point ends in one of three states: *decided*, *scope changed* or *accepted risk* (with the user saying they accept it). The PRD has no "open questions" section. If something depends on someone outside (a partner, a supplier), it becomes an accepted risk with an owner and a deadline, and you can offer a separate document of questions for that person.
2. **Questions in short rounds, with options.** At most 4 questions per round, each with alternatives (A, B, C) and one marked as recommended, plus room for a free answer. Choosing is fast; writing from scratch is tiring and makes people quit halfway. Ask first what changes the product the most.
3. **Don't make up numbers.** Market size, competitor prices and conversion rates only appear with a source (search, if there's a search tool, and cite it) or marked as a *hypothesis to validate*. An investor who invents data takes the credibility of the whole board with her.
4. **Assumptions stay visible.** Whatever you inferred without the user confirming shows up in the decision sheet as an assumption, before the gate, for them to confirm or correct.
5. **Tone:** direct, no artificial enthusiasm, no empty praise. Follow the writing preferences in the profile (by default, no em dashes).
6. **Living log:** if you have file access, keep `idea.md` in the output folder and update it at the end of each phase (format in `references/process.md`). Consultative conversations get long and context can be summarized; the file guarantees no decision gets lost. No need to show the file at every update, one line saying so is enough.

## 5. Consultative mode

Read `references/process.md` (the phases, with exit criteria) and `references/board.md` (who each persona is, how they talk, the chat format and the anti-flattery rules). The questions for each block are in `references/interview.md` and the stack conversation in `references/stack.md`.

Phase summary:

0. **Triage:** pitch in one or two sentences, document type (new product, feature, technical), mode.
1. **Understanding:** problem, audience, solution, current alternative, why now. Ends when the positioning statement is confirmed.
2. **Board, round 1:** Téo opens, each persona gives a signal, main objection and one question. Téo consolidates the questions.
3. **Rebuttals:** the user answers, personas react only to what changed, the objection board is updated. Up to 3 rounds.
4. **Convergence:** MVP scope (in and out), main flows, data, stack, success metric.
5. **Verdict and gate:** each persona's final signal and the decision sheet. Only continues with explicit confirmation.
6. **Generation.**

## 6. Fast mode

The goal is to reach the document in 2 to 4 messages without giving up on settling every doubt.

1. Read what the user brought (text, file, repository).
2. Compare it with the minimum to generate (list in `references/prd-template.md`, section "Minimum to generate"). In a single message, show:
   - **Lightning opinion:** one line per persona (Helena, Caio, the ideal customer, Bia or Lucas, and Lúcia if there's a trigger), with signal and the most important point. It's a warning, not an interrogation. If a red shows up, say so clearly and offer to switch to consultative.
   - **Gaps:** a single round, only with what **blocks the build**. Whatever can be decided with a sensible default, decide and record as an assumption.
3. Decision sheet (format in `references/process.md`, phase 5) and gate. If the material is complete with no gaps, the sheet goes in the same message as the opinion.
4. Generation.

## 7. Make the conversation more visual (if the environment allows)

The process works with text only, but it gets better when the environment offers more. Use what exists, without announcing the tool:

- **Clickable option questions** (when the assistant has a tool for questions with choices): use them in the question rounds. Each question becomes a card with 2 to 4 options, the recommended one first and labeled "(recommended)"; the free-answer option is usually automatic, don't repeat it. The personas' lines stay in the text, before the questions.
- **Visuals in the chat** (widgets, artifacts, canvas or rendered pages): use them at two moments only, the **board's verdict** and the **decision sheet**. Render the persona cards with each one's color (see `references/board.md`). Don't render every round: it costs time and clutters the conversation.
- **Text only:** use the markdown line format from `references/board.md`, with the emoji and the persona's name in the header.

## 8. Generate the files

Only after the gate. In this order:

1. **`PRD.md`**: the source of truth, written to be read by a coding agent. Structure and quality checklist in `references/prd-template.md`.
2. **`PRD.html`**: the same content, with the skeleton's look and the board's verdict with avatars. Always start from `assets/skeleton.html` and follow `references/html.md`. The HTML is derived from the MD: if they diverge, the MD wins.
3. **`PLAN.md`** (when the user asks, or offer it at the end): phases in dependency order, tasks with done criteria and a handoff prompt to paste into the agent. Format in `references/plan-template.md`.

**Board photos in the HTML:** if you can run Python, run `python3 <skill folder>/scripts/embed_avatars.py <path to PRD.html>`, which embeds the images from `assets/board/` into the file. If you can't, use the published photos, with `<img>` pointing to `https://raw.githubusercontent.com/JefersonMarcioEspindola/skill-prd-consultive/main/plugins/prd-consultive/skills/prd-consultive/assets/board/<persona>-<signal>.webp` (details in `references/html.md`). They show up when the file is opened online. As a last resort, the cards show colored initials.

**Where to deliver:** depends on the environment.

- **With folder access** (coding agents): save in the folder set in the profile; without a profile, in `prd/<product-name>/` in the current working folder.
- **Chat app that creates downloadable files** (for example, with code execution or an output folder): create the files and deliver them as downloads.
- **Chat app without files:** show `PRD.md` in a markdown code block (or canvas, if available), and `PRD.html` in a separate `html` code block, telling the user to save it with that name and open it in a browser. If the app has a canvas or artifact that renders HTML, use it.

Outside that last case, never paste the whole HTML into the chat.

**Final message:** short. Say which files were created, which to use for what (the `.md` goes to the agent or the chat, the `.html` is for reading and sharing) and the concrete next step, for example: paste the handoff prompt from `PLAN.md` into the coding agent (Claude Code, Codex, Cursor).

## File map

| File | When to read |
|---|---|
| `profile.md` | Always, at the start |
| `references/process.md` | Consultative mode: phases, exit criteria, decision sheet, `idea.md` |
| `references/board.md` | Whenever a persona speaks |
| `references/interview.md` | When putting together a round of questions |
| `references/stack.md` | In convergence, or when the stack isn't clear |
| `references/prd-template.md` | Before writing `PRD.md`, and in fast mode to check gaps |
| `references/html.md` | Before writing `PRD.html` |
| `references/plan-template.md` | Before writing `PLAN.md` |
| `assets/skeleton.html` | Base for every generated HTML |
| `scripts/embed_avatars.py` | After saving `PRD.html`, if you can run Python |
