# AGENTS.md — 02-asis (Phase 2: new As-Is documentation)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Goal
Extract what the **newly documented As-Is** says, as cited KUs, and show how it differs from the legacy docs.

## Inputs
- `00-context/sources.md` (corpus = as-is), `input/raw/` and/or MCP
- `01-legacy/output/knowledge/` (for the delta, if available)
- Spike scope, domain glossary

## Outputs
- `output/inventory.md`
- `output/knowledge/<P-PROC>.md`
- `output/legacy-delta.md`: per process, KUs that are **new**, **changed**, **unchanged**, or **dropped** compared with legacy

## Rules
- Read `RULES.md` first.
- The As-Is docs are owned by Alejandra's team. Preserve their structure (process → steps) in the `step` field.
- If an As-Is doc describes intent ("should", "debe") rather than behavior, keep the wording and set `confidence: M`.
- The delta is informational. It is **not** a judgment of correctness.

## Done-criteria (G2)
- All in-scope As-Is docs processed. The delta is produced if legacy KUs exist.
- Alejandra approves the sample and all L-confidence items.
