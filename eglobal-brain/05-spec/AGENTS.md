# AGENTS.md — 05-spec (Phase 5: To-Be specification)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Goal
Turn the validated As-Is and the To-Be goals into a **PRD** (why/what) and an **SDD** (requirements → design → tasks), plus an **AGENTS.md** that lets agents and developers build each capability.

## Folder layout
```
05-spec/CAP-###-<slug>/
  prd.md       (templates/prd.md)
  sdd.md       (templates/sdd.md)
  AGENTS.md    (templates/subprocess-AGENTS.md)
```

## Inputs
- `04-audit/output/validated-asis/` (approved only)
- `04-audit/output/audit-report.md` (recommendations)
- `00-context/project-charter.md`, `00-context/architecture/*`
- To-Be goals from the business owner (interview if missing)

## Rules
- Read `RULES.md` first.
- Every PRD goal and SDD requirement traces back to validated As-Is KUs, a decision, or an explicit To-Be goal (`source:`).
- Requirements use **EARS** ("When <trigger>, the system shall <response>") with testable acceptance criteria.
- Mark explicitly what **changes** from the As-Is (`change: new | modified | retired | unchanged`).
- The SDD design must reference `00-context/architecture/`. If those files are still 🟥, write the design as "provisional" and list what's missing.

## Done-criteria
- G5a: PRD approved by the business owner.
- G5b: SDD + AGENTS.md approved by the Tech Lead / Architect.
