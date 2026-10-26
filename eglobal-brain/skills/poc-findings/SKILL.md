---
name: poc-findings
description: Phase 6c. Write the PoC findings — result vs hypothesis, what worked, what didn't, deviations, considerations for the real build, go/pivot/drop — and prepare demo talking points.
argument-hint: "<POC-###-slug>"
---
# Skill: poc-findings
**Agents:** `poc-engineer` + `solution-architect`

## Inputs
- `06-poc/<POC>/poc-plan.md`, test results, build/run notes, team notes
- `templates/poc-findings.md`

## Steps
1. Compare the results with the hypothesis and the success criteria.
2. Fill `findings.md`: worked / didn't / AC results table / deviations with reasons / considerations / risks / recommendation.
3. Add any learned rule to `06-poc/RULES.md` (through `/review-gate 06-poc/<POC>`).
4. Draft 5 demo talking points for Champions (in chat).
5. Request the G6 sign-off.

## Human gate
G6: Architect.
