# AGENTS.md — 04-audit (Phase 4: cross-reference → validated As-Is)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Goal
Compare the KUs from legacy, As-Is, and code. Classify every match and gap. Help the humans resolve the conflicts. Publish the **validated As-Is** and the **audit report**.

## Inputs
- Approved KUs: `01-legacy/output/knowledge/`, `02-asis/output/knowledge/`, `03-code/output/knowledge/`
- `00-context/domain-glossary.md`, `guide/03-knowledge-schema.md` (taxonomy and matching rules)
- `spikes/<SPIKE>/validation-process.md`

## Outputs
- `spikes/SPIKE-###/validation-process.md` (Phase 0 output, designed before executing)
- `output/traceability-matrix.csv`, columns: `match_id,process,step,type,statement,ku_legacy,ku_asis,ku_code,category,disc_id,confidence,decision_ref`
- `output/discrepancies/DISC-<PROC>-###.md`: one per ⚠️ 🕳️ 👻 ❓
- `output/validated-asis/<P-PROC>.md`
- `output/audit-report.md`
- `review/decision-log.md`

## Rules
- Read `RULES.md` first.
- **Never resolve ⚠️ or ❓ yourself.** Give the evidence from every source and a recommendation, and leave the decision to humans.
- When legacy and the As-Is disagree but the code agrees with one of them, say so explicitly. It is strong evidence, not a decision.
- The validated As-Is contains **only** ✅ items and items resolved by a human decision (cite `decision:`).
- Report coverage honestly: % of As-Is KUs found in code, % of code KUs documented.

## Done-criteria (G4)
- Every in-scope KU appears in the matrix.
- Every ⚠️/❓ has a decision in `review/decision-log.md`.
- Validated As-Is + audit report signed off by Alejandra **and** the Tech Lead.
