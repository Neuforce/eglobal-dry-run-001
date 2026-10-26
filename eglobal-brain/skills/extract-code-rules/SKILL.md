---
name: extract-code-rules
description: Phase 3. Use the GitHub MCP (read-only) to map in-scope processes to code and extract business rules, validations, calculations, entities and integrations as cited Knowledge Units into 03-code/output/.
argument-hint: "<SPIKE-###>"
---
# Skill: extract-code-rules
**Agent:** `code-archaeologist`

## Inputs
- The spike's validation process (strategy!)
- `00-context/repos.md` (repos, branch, mapping, exclusions)
- GitHub MCP tools (read-only)
- docs→code strategy: `02-asis/output/knowledge/<P-PROC>.md` as the search list
- Domain glossary, `03-code/RULES.md`, `03-code/AGENTS.md`

## Preconditions
- G0 approved. The GitHub MCP is reachable. `repos.md` lists at least one in-scope repo.

## Steps
1. Read `03-code/AGENTS.md` and `RULES.md`. Resolve the branch to a commit SHA and use that SHA in **every** citation.
2. **Map:** starting from the module ↔ process mapping (or, if missing, by searching glossary terms and identifiers), find the entry points (APIs, jobs, consumers, UI handlers) and trace the call chains. Write `03-code/output/code-map.md` (`templates/code-map.md`). If you proposed the mapping yourself, flag it for the Tech Lead.
3. **Extract:**
   - *docs→code:* for each As-Is KU, search for the implementing logic and write a code KU (same step/type) or note "not found" (a candidate 👻).
   - *code→docs:* walk the mapped modules and extract every business-relevant rule (candidates 🕳️ included).
   - Statements in business language. Citations `code:<repo>/<path>:<l1>-<l2>@<sha>`, excerpt ≤ 3 lines.
   - Capture constants and config, with their source. Note runtime-configurable values.
4. Write `03-code/output/knowledge/<P-PROC>.md` (banner 🟨).
5. Run `/verify-citations`.
6. Report: entry points, KUs by type, "not found" list, observations (dead code, hard-coded values). Suggest `/review-gate 03-code`.

## Output
`03-code/output/code-map.md`, `03-code/output/knowledge/<P-PROC>.md`

## Human gate
G3: Tech Lead.

## Common failures
- Rate limits / large repos: narrow to the mapped paths and use code search before reading files.
- Logic in DB stored procedures or config not on GitHub: record it as an open question with `confidence: L`.
