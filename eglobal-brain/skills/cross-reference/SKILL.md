---
name: cross-reference
description: Phase 4. Match approved Knowledge Units across legacy, As-Is and code; classify each as ✅ Confirmed, ⚠️ Drift, 🕳️ Undocumented, 👻 Orphan or ❓ Ambiguous; write the traceability matrix and one discrepancy record per non-✅ item.
argument-hint: "<SPIKE-###>"
---
# Skill: cross-reference
**Agents:** `auditor` (matching and classification), then `verifier` (sample check)

## Inputs
- Approved KUs: `01-legacy/`, `02-asis/`, `03-code/` `output/knowledge/<P-PROC>.md`
- `guide/03-knowledge-schema.md` (taxonomy + matching rules), domain glossary
- `04-audit/RULES.md`, `04-audit/AGENTS.md`

## Preconditions
- G1, G2, and G3 passed for the in-scope processes (check the review logs). If one is missing, list it and stop, unless the user explicitly accepts running on unapproved KUs (then label every output "PRELIMINARY").

## Steps
1. Load the KUs. Group them by process → step → type.
2. Match them using the matching rules (glossary synonyms included). Create a `match_id` per cluster.
3. Classify each cluster:
   - ✅ legacy/As-Is statement ≡ code statement (same conditions, values, outcomes)
   - ⚠️ present in docs and code but different in any condition, value, or outcome
   - 🕳️ code only · 👻 docs only · ❓ evidence is insufficient or contradictory
   - Note when legacy ≠ As-Is and the code sides with one of them.
4. Write `04-audit/output/traceability-matrix.csv` (columns in `04-audit/AGENTS.md`).
5. For every non-✅ item, write `04-audit/output/discrepancies/DISC-<PROC>-###.md` (`templates/discrepancy.md`), with the evidence, the analysis, and a **non-binding** recommendation. Set impact H/M/L.
6. Ask `verifier` to re-check 10% of the ✅ matches and every H-impact DISC.
7. Report the counts per category, the top 5 H-impact items, and the proposed agenda for the joint gate session.

## Output
Traceability matrix + DISC records

## Human gate
Next: `/review-gate 04-audit` (joint session).
