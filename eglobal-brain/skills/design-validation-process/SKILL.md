---
name: design-validation-process
description: Phase 0 spike design. Before validating anything, design HOW a spike will validate one As-Is process — scope, strategy (docs→code, code→docs, hybrid), steps, sampling — and write it to 04-audit/spikes/SPIKE-###/validation-process.md.
argument-hint: "<SPIKE-###> <P-PROC>"
---
# Skill: design-validation-process

## When to use
At the start of every spike. The first deliverable of a spike is its process, not its findings.

## Inputs
- `00-context/process-inventory.md`, `sources.md`, `repos.md`, `project-charter.md`
- `guide/01-methodology.md` (strategies)
- Previous spikes' retrospectives (`04-audit/spikes/*/validation-process.md` §8), if any

## Preconditions
- `process-inventory.md`, `sources.md`, and `repos.md` are not 🟥 for the target process. If they are, stop and point to `/setup-context`.

## Steps
1. Confirm the process ID with the user. If none was given, propose 1–3 candidates from the inventory (spike candidate = Y, ranked by criticality, documentation quality, and code footprint) and ask.
2. Size the scope: steps in scope, sources, repos/paths. Recommend splitting if the scope covers more than ~2 repos or more than ~8 steps.
3. Recommend a strategy with a rationale:
   - The As-Is docs are recent and structured → **docs→code**
   - The docs are weak, or the module is small and critical → **code→docs**
   - Broad scope → **hybrid**
4. Fill in `templates/validation-process.md` → `04-audit/spikes/<SPIKE>/validation-process.md` (sampling from `guide/02-human-in-the-loop.md`, timebox from the charter).
5. List the risks and assumptions explicitly.
6. Present a short summary and ask for the G0 approval.

## Output
`04-audit/spikes/<SPIKE>/validation-process.md` (banner 🟨)

## Human gate
G0 (part 2): Alejandra + Tech Lead. Record it in `04-audit/review/decision-log.md`.

## Done-criteria
Scope, strategy, steps, sampling, and timebox approved.
