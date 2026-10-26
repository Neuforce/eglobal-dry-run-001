---
name: audit-report
description: Phase 4 close. Compile the validated As-Is per process (only ✅ and human-resolved items) and the audit report with coverage metrics, findings, risks and To-Be recommendations.
argument-hint: "<SPIKE-###>"
---
# Skill: audit-report
**Agent:** `auditor`

## Inputs
- `04-audit/output/traceability-matrix.csv`, `discrepancies/*`, `review/decision-log.md`
- Approved KUs (all three corpora), `01-legacy/output/inventory.md`, `02-asis/output/legacy-delta.md`, `03-code/output/code-map.md`
- `templates/validated-asis.md`, `templates/audit-report.md`

## Preconditions
- Every ⚠️ and ❓ in scope has a decision. If not, list the pending ones and stop.

## Steps
1. For each process, build `04-audit/output/validated-asis/<P-PROC>.md`:
   - Rules = ✅ matches + human decisions (cite `decision:`). Number them `VR-<PROC>-###`.
   - Flow diagram (Mermaid) from the steps. Entities and integrations from the code map and KUs.
   - Known gaps: unresolved 🕳️ / 👻 marked "document" or "investigate".
   - Coverage percentages.
2. Build or update `04-audit/output/audit-report.md`: metrics table, key findings (H-impact first), risk heatmap, To-Be recommendations, method retrospective (rules learned, gate accuracy).
3. Fill §8 (Retrospective) of the spike's `validation-process.md`.
4. Report and request the G4 sign-off.

## Human gate
G4: Alejandra **and** Tech Lead.
