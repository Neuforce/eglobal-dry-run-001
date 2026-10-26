# Methodology

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## The problem
Three sources describe the same system and disagree:
1. **Legacy documentation**: old, scattered, partly obsolete.
2. **New As-Is documentation**: recent, written by people, may reflect intent rather than reality.
3. **Code**: what actually runs, but hard for business people to read.

Building the To-Be on an unvalidated As-Is carries those errors into the new system.

## The idea
Normalize all three sources into the **same unit**, the *Knowledge Unit* (see `03-knowledge-schema.md`). Then compare them item by item, and let humans decide every conflict.

## Phases
| # | Phase | Main question | Output |
|---|---|---|---|
| 0 | Setup + spike design | What will we validate, and how? | `00-context/` filled, `validation-process.md` |
| 1 | Legacy | What did the old docs say? | Legacy KUs |
| 2 | As-Is | What do the new docs say, and what changed? | As-Is KUs + delta |
| 3 | Code | What does the system actually do? | Code KUs + code map |
| 4 | Audit | Where do they agree or disagree, and who is right? | Validated As-Is + audit report |
| 5 | Spec | What should the To-Be do? | PRD, SDD, subprocess AGENTS.md |
| 6 | PoC | Does it work on our platform? | Containerized PoC + findings |

## Two validation strategies (chosen per spike in Phase 0)
- **docs→code:** Start from the documented As-Is and look for each rule in the code. Best when the As-Is docs are recent and well structured. It finds ⚠️ Drift and 👻 Orphan items quickly.
- **code→docs:** First extract the rules from the code for a bounded module, then interpret the docs against them. Best when the docs are weak or the module is small. It finds 🕳️ Undocumented logic.
- **Hybrid (default for broad scopes):** docs→code for the main flow, code→docs for critical modules.

## Spikes
Work in small, timeboxed **spikes**: one process (or sub-process) at a time. The first spike validates the method itself. Its first output is the *process* it will follow (`validation-process.md`), designed before anything is executed. Every spike adds rules (`RULES.md`) and knowledge that the next spikes reuse.

## Why this works
- **LLMs** are fast and tireless at reading, extracting, and comparing.
- **Humans** bring judgment, context, and accountability.
- **The repo** remembers everything, so knowledge builds up instead of staying in people's heads or in chat history.
