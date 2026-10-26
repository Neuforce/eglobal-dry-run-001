---
name: write-sdd
description: Phase 5b. Turn an approved PRD into a Spec-Driven Development package — EARS requirements with acceptance criteria, design aligned to eGlobal architecture, tasks — plus the capability's AGENTS.md.
argument-hint: "<CAP-###-slug>"
---
# Skill: write-sdd
**Agents:** `spec-writer` (requirements, tasks) + `solution-architect` (design)

## Inputs
- `05-spec/<CAP>/prd.md` (approved), the related validated As-Is
- `00-context/architecture/**`
- `templates/sdd.md`, `templates/subprocess-AGENTS.md`

## Preconditions
- The PRD is approved (G5a).
- If any `architecture/*` file is still 🟥, warn the user. The design gets `Design status: provisional` and the missing inputs are listed.

## Steps
1. **Requirements:** derive `REQ-###` items in EARS form from the PRD scope and the validated rules. Each one has a source, a change type, and ≥ 1 testable acceptance criterion (Given/When/Then). Add NFRs from `nfrs.md`.
2. **Design** (solution-architect): components, data model, contracts, sequences, integrations, security/observability. Everything conforms to `standards.md` and `target-architecture.md`. Record significant choices as ADRs in `00-context/architecture/adr/`.
3. **Tasks:** break the design into tasks referencing the REQs. Mark a candidate PoC slice (the riskiest assumptions first).
4. Write `05-spec/<CAP>/sdd.md`, then generate `05-spec/<CAP>/AGENTS.md` from `templates/subprocess-AGENTS.md` (business rules that are easy to get wrong go in "Rules you must obey").
5. Request G5b.

## Human gate
G5b: Tech Lead / Architect.
