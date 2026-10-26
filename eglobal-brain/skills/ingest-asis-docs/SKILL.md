---
name: ingest-asis-docs
description: Phase 2. Read the newly documented As-Is (Alejandra's team) from 02-asis/input/raw/ or MCP, extract cited Knowledge Units per process, and produce a delta versus legacy KUs.
argument-hint: "<SPIKE-###>"
---
# Skill: ingest-asis-docs
**Agent:** `doc-analyst`

## Inputs
- The spike's validation process, `00-context/sources.md` (corpus = as-is)
- `02-asis/input/raw/**` and/or the MCP doc tools
- `01-legacy/output/knowledge/<P-PROC>.md` (if available)
- Domain glossary, `02-asis/RULES.md`, `02-asis/AGENTS.md`

## Preconditions
- G0 approved. The As-Is source is reachable.

## Steps
1. Read `02-asis/AGENTS.md` and `RULES.md`.
2. Build the inventory → `02-asis/output/inventory.md`.
3. Extract KUs (same procedure as `ingest-legacy-docs`). Keep the As-Is step structure in `step`. Intent wording ("debe") gets `confidence: M`.
4. If legacy KUs exist, compute the delta per process (new / changed / unchanged / dropped) → `02-asis/output/legacy-delta.md` (`templates/legacy-delta.md`).
5. Run `/verify-citations`.
6. Report the counts. Suggest `/review-gate 02-asis` (owner: Alejandra).

## Output
`02-asis/output/inventory.md`, `knowledge/<P-PROC>.md`, `legacy-delta.md`

## Human gate
G2: Alejandra.
