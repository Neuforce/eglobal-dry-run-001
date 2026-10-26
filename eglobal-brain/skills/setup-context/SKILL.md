---
name: setup-context
description: Phase 0. Interview the Tech Lead / As-Is owner to fill the 🟥 REQUIRED files in 00-context/, confirm or correct the 🟨 assumptions, and produce a readiness report. Use at project start, or with the argument "architecture" before Phase 5b/6.
argument-hint: "[all | architecture | <file>]"
---
# Skill: setup-context

## When to use
At the start of the project (Step 1 of `guide/00-prompt-guide.md`), or later to fill a specific context file (e.g. `architecture`).

## Inputs
- `00-context/**` (templates with 🟥/🟨 banners)
- `00-context/open-questions.md`

## Preconditions
- None. This is the first skill.

## Steps
1. Run `scripts/review-status.sh 00-context` (or scan the banners) and list the 🟥 and 🟨 files in scope for the argument.
2. For each 🟥 file, in this order: `stakeholders` → `process-inventory` → `sources` → `repos` → `domain-glossary` → `architecture/*`:
   - Explain in 1–2 lines what the file is for and the minimum needed.
   - Ask **short, grouped questions** (max 5 at a time). Accept "don't know". Record it as `TBD` and add a question to `open-questions.md`.
   - Write the answers into the template. Do not invent anything. Note the provenance ("per <name>, <date>").
   - If the user points to a source (link, doc, MCP), read it and propose the content for confirmation.
3. For each 🟨 file, show the "Assumptions in this file" list and ask: confirm / correct. Apply the corrections.
4. Once a 🟥 file is substantially filled, change its banner to `🟨 ASSUMPTION — provided by <name>, review & approve`. **Never** set `✅ APPROVED`.
5. Smoke-test the connectors: list one repo from `repos.md` through the GitHub MCP and one document from each MCP source in `sources.md`.
6. Write the readiness report in chat, and append a summary to `STATUS.md`.

## Output
- Updated `00-context/**`, `open-questions.md`, `STATUS.md`

## Human gate
G0 (part 1): the Tech Lead + Alejandra approve the context files and set the banners to ✅.

## Done-criteria
- No 🟥 files left outside `architecture/` (or all of them, for `architecture`).
- Connectors verified, or the fallback (file drop) documented in `sources.md`.

## Common failures
- The user doesn't know the module ↔ process mapping → record the repos only. `extract-code-rules` will propose a mapping for review.
