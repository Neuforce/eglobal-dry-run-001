<!--
PURPOSE:     Designs HOW a spike will validate the As-Is, BEFORE executing anything.
OWNER:       Tech Lead + Alejandra (approve) · drafted by /design-validation-process
CONSUMED BY: every skill run for this spike
-->
# SPIKE-###: Validation Process for <P-PROC> <process name>

> **🟨 ASSUMPTION — review & approve.** Drafted by agent. **Approver:** Alejandra + Tech Lead · **Blocks:** Phases 1–4 for this spike

## 1. Goal
<!-- What we want to learn or validate, in one paragraph -->

## 2. Scope
- **Process(es):** P-XXX (steps in scope: …)
- **Out of scope:** …
- **Sources:** SRC-xx (legacy), SRC-yy (as-is)
- **Repos / modules:** org/repo → paths

## 3. Strategy
- [ ] docs→code  [ ] code→docs  [ ] hybrid
- **Why:** <!-- based on doc quality, module size, risk -->

## 4. Steps
| # | Step | Skill | Output | Gate |
|---|---|---|---|---|
| 1 | Legacy extraction | ingest-legacy-docs | 01-legacy/output/knowledge/P-XXX.md | G1 |
| 2 | As-Is extraction | ingest-asis-docs | 02-asis/output/knowledge/P-XXX.md | G2 |
| 3 | Code extraction | extract-code-rules | 03-code/output/knowledge/P-XXX.md | G3 |
| 4 | Cross-reference | cross-reference | matrix + DISC | — |
| 5 | Joint review | review-gate | decision-log | G4 |
| 6 | Audit report | audit-report | validated-asis/P-XXX.md | G4 |

## 5. Sampling and acceptance
- Sample size per gate: … · Accuracy threshold: ≥ 90%
- Always reviewed: ⚠️, ❓, confidence L

## 6. Risks and assumptions
| Risk / assumption | Mitigation |
|---|---|

## 7. Timebox
- Start: · Target G4:

## 8. Retrospective (fill at the end)
- What worked · what to change in skills/rules · rules added
