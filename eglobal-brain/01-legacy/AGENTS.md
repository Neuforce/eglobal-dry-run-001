# AGENTS.md — 01-legacy (Phase 1: legacy documentation)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Goal
Extract what the **legacy documentation** says about the in-scope processes, as cited Knowledge Units.

## Inputs
- `00-context/sources.md` (rows with corpus = legacy)
- `input/raw/` (exported files) **and/or** an MCP doc source
- `04-audit/spikes/<SPIKE>/validation-process.md` (scope)
- `00-context/domain-glossary.md`

## Outputs
- `output/inventory.md` (template: inventory table in `templates/inventory.md`)
- `output/knowledge/<P-PROC>.md` (KUs, template `templates/knowledge-unit.md`)

## Rules
- Read `RULES.md` first.
- Legacy docs can be outdated. Record the doc date on every KU source, and **do not** judge correctness here (that is Phase 4).
- Flag contradictions **between legacy docs** as KUs with `related:` links and a `confidence: L` note.
- Propose new glossary terms in a "Proposed glossary terms" section at the end of each knowledge file.
- Only process documents relevant to the spike scope. List the skipped ones in the inventory with a reason.

## Done-criteria (G1)
- Every in-scope source is listed in the inventory (processed or skipped, with a reason).
- Every KU has a citation and an excerpt.
- SME sample review ≥ 90% accurate (see `guide/02-human-in-the-loop.md`).
