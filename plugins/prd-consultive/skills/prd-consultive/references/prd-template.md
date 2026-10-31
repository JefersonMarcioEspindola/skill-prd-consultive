# PRD.md template

`PRD.md` is the source of truth and is written for two readers: a person who will decide and a coding agent who will build. For the agent, what matters is no ambiguity: stable IDs, testable requirements, decisions with the why and clear limits on what **not** to do.

Write the PRD in the session's language. The headings below are in English; translate them (in Portuguese, for example: Resumo, Problema e contexto, Público, Objetivos e métricas, Escopo do MVP...). Keep the IDs as they are (FR-01, NFR-01, D-01, R-01, E-01) in any language, so the PLAN and the agent can reference them.

## Contents

- Minimum to generate
- Writing principles
- Structure
- Variations by document type
- Checklist before saving

---

## Minimum to generate

Without these items the PRD comes out vague. In fast mode, this is the list you check gaps against:

1. Main audience, specific
2. Problem and current alternative
3. What's in the MVP **and what's out**
4. Main flow, step by step
5. Main data entities
6. Stack (or an accepted recommendation)
7. Main success metric

## Writing principles

- **A section that doesn't change the build or a product decision doesn't go in.** A precise 4-page PRD beats a generic 15-page one.
- **Requirements use "must"** and have a verifiable acceptance criterion. "Must be fast" isn't a criterion; "the client list loads in under 1 s with 500 records" is.
- **Stable IDs** (FR-01, NFR-01, D-01, R-01, E-01) so PLAN.md and the agent can reference them. FR = functional requirement, NFR = non-functional requirement, D = decision, R = accepted risk, E = entity.
- **Acceptance criteria as a numbered list, never checkboxes.** The PRD is a specification, not a task list: the reader is an agent, and it needs to cite the criterion ("FR-03, criterion 2"), not tick it. Checkboxes only exist in PLAN.md, where the agent marks what it finished.
- **Every decision has the why and the rejected alternative.** That's what stops the agent (or you, three months from now) from "improving" something that was decided on purpose.
- **Realistic timelines for people who build with AI.** Build order is in phases, not weeks. If the document mentions time, separate build time (hours or days with an agent) from waiting on third parties (approvals, reviews, activations), which is usually what sets the date.
- **Out of scope is as important as scope.** Agents love adding things; the "out" list is the brake.
- **No open questions.** Anything left pending appears as an accepted risk, with an owner and a review trigger.
- Follow the tone and writing rules in the profile.

## Structure

Use these headings, in this order (translated into the session's language). The numbers help with references ("see section 7").

```markdown
# <Product>: PRD

> **Status:** approved by the board on <date> · **Mode:** <fast | consultative> · **Type:** <new product | feature | technical> · **Version:** 1.0

## 1. Summary
<Positioning statement, in bold.>
<One paragraph: what it is, for whom, what it solves and what makes it different.>

## 2. Problem and context
- **Pain:** <the pain, from the point of view of the person who suffers from it>
- **How it's solved today:** <current alternative and what's bad about it>
- **Why now:** <what changed>

## 3. Audience
<Main user, with usage context (device, moment, comfort with technology). If the payer differs from the user, say so.>
<Other user profiles (admin etc.) in a short list.>

## 4. Goals and metrics
| Metric | Target | Deadline | How to measure |
|---|---|---|---|
| <main> | | | |

**Non-goals:** <what the product deliberately doesn't try to be or solve>

## 5. MVP scope
**In:**
- <item> (FR-xx)

**Out (and why):**
- <item>: <short reason; when to revisit>

## 6. Main flows
### F1. <flow name>
1. <step, from the user's point of view>
2. ...
**Result:** <end state>

## 7. Functional requirements
### FR-01. <short name>
<The system must...>
**Acceptance criteria:**
1. <verifiable behavior>
2. <error or edge case>
**Priority:** <essential | important> · **Flow:** F1

## 8. Non-functional requirements
- **NFR-01 Security:** <...>
- **NFR-02 Privacy (LGPD, GDPR or the local law):** <...>
- **NFR-03 Performance:** <...>
- **NFR-04 Accessibility:** <...>
<Only the ones that apply, each verifiable.>

## 9. Data model
| Entity | Main fields | Relations |
|---|---|---|
| `E-01 Name` | <fields> | <belongs to / has many> |

## 10. Stack and architecture
| Layer | Choice | Why |
|---|---|---|
<A short architecture paragraph, if there's anything beyond the obvious (queues, jobs, integrations).>

## 11. Decisions
- **D-01:** <decision>. Because <reason>. Rejected: <alternative>.

## 12. Accepted risks
| ID | Risk | Raised by | Mitigation | Revisit when |
|---|---|---|---|---|

## 13. Board verdict
| Persona | Signal | Main point | How it was handled |
|---|---|---|---|
| Helena · Investor | 🟢 | | |
| Caio · Senior dev | 🟡 | | |
| Bia · Ideal customer | 🟢 | | |

## 14. Build order
1. <phase>: <what it delivers> (FR-xx, FR-yy)
<Same sequence as PLAN.md, if it exists.>
```

## Variations by document type

- **Feature in an existing product:** section 3 becomes "Who's affected" (can be short); section 9 shows only new or changed entities; add "Impact on what exists" after section 6 (screens, APIs and data that change and how to migrate).
- **Technical or refactor:** section 2 becomes "Current situation and technical problem"; sections 3 and 6 can go; add "Migration and rollback plan" after section 10; metrics are technical (build time, cost, errors), but at least one has to tie the change to the business.
- **Fast mode:** section 13 carries the lightning opinion (one line per persona). Say so in the section itself.

## Checklist before saving

Reread the PRD against this list. If anything fails, fix it before delivering.

- [ ] The whole document is in the session's language, including headings and labels.
- [ ] No open questions, no "to be defined", no "TBD".
- [ ] Every FR has at least one verifiable acceptance criterion and an error case when there's user input.
- [ ] Every "In" scope item points to an FR, and every FR is in scope.
- [ ] The "Out" list exists with a reason on each item, and nothing that's out is promised elsewhere (summary, positioning, flows).
- [ ] Every decision has the why.
- [ ] The build order doesn't contradict dependencies (you don't build payments before the sign-up they use).
- [ ] The board verdict is what it actually said, without softening red signals.
- [ ] No market number without a source or the hypothesis label.
- [ ] No code estimate in weeks or months; when there's third-party waiting, it appears separately, with the request starting in Phase 1.
- [ ] Nothing in the document that isn't in the decision sheet or in `idea.md`.
