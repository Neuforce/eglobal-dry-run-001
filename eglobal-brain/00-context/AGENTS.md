# AGENTS.md — 00-context (Phase 0 inputs)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Scope
This folder holds the **inputs** every other phase depends on. Humans own it.

## Rules for agents
- **Never invent content** in files marked `🟥 REQUIRED`. Fill them only from what a human tells you (interview through `/setup-context`) or from sources a human points you to. Cite where each answer came from (e.g. "per Alejandra, 2026-10-08").
- In `🟨 ASSUMPTION` files, keep the "Assumptions in this file" list current. When a human confirms or corrects an assumption, update it and note who and when.
- Unknowns go to `open-questions.md`. Do not leave silent gaps.

## Done-criteria (Gate G0)
- No 🟥 files left outside `architecture/` (architecture is needed before Phase 5b / 6).
- `process-inventory.md` has at least one process marked as the spike candidate.
- `sources.md` and `repos.md` cover the spike candidate.
- 🟨 files approved by their owners (see `README.md`).
