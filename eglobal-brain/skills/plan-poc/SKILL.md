---
name: plan-poc
description: Phase 6a. Plan a minimal PoC (1–2 containers) from an approved SDD and the architecture inputs. Refuses to run while 00-context/architecture/ still has 🟥 REQUIRED files.
argument-hint: "<POC-###-slug> <CAP-###-slug>"
---
# Skill: plan-poc
**Agent:** `solution-architect`

## Inputs
- `05-spec/<CAP>/sdd.md` (approved), `00-context/architecture/**`, `adr/ADR-001-poc-approach.md`
- `templates/poc-plan.md`, `06-poc/RULES.md`, `06-poc/AGENTS.md`

## Preconditions (hard)
1. Run `scripts/review-status.sh 00-context/architecture`. If **any** 🟥 is reported → **STOP**. List the files and the minimum needed (see `00-context/architecture/README.md`), and suggest `/setup-context architecture`.
2. The SDD is approved (G5b).

## Steps
1. Pick the slice: the tasks marked as PoC candidates, the riskiest assumptions first. Confirm with the user.
2. Write the hypothesis in the template's form.
3. Define the containers (≤ 2), the base images, and the resources, per `platform-openshift.md`.
4. Decide real vs mock for each integration (per `integration-catalog.md` "Mock allowed").
5. Define the success criteria (ACs + any NFR demo) and the compliance checklist.
6. Write `06-poc/<POC>/poc-plan.md`. Request G6 (plan).

## Human gate
G6 (plan): Architect.
