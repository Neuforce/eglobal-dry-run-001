---
name: write-prd
description: Phase 5a. Draft a PRD for a To-Be capability from the validated As-Is, audit recommendations and business To-Be goals, with full traceability.
argument-hint: "<CAP-###-slug>"
---
# Skill: write-prd
**Agent:** `spec-writer`

## Inputs
- `04-audit/output/validated-asis/*.md` (approved), `audit-report.md`
- `00-context/project-charter.md`, `stakeholders.md`
- The business owner's To-Be goals (interview if they aren't documented)
- `templates/prd.md`, `05-spec/RULES.md`, `05-spec/AGENTS.md`

## Preconditions
- The related validated As-Is is ✅ APPROVED. Otherwise, warn the user and label the PRD "PROVISIONAL".

## Steps
1. Confirm the capability scope with the user (which processes/steps, which business outcome).
2. If the To-Be goals are missing, interview the business owner: problem, users, goals plus metrics, non-goals, constraints (max 5 questions at a time).
3. Draft `05-spec/<CAP>/prd.md`. Every goal and rule row cites a `VR-…`, a decision, or a stated goal. Mark the change type per scope item.
4. List the open questions. Request G5a.

## Human gate
G5a: business owner.
