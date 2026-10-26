---
name: ingest-legacy-docs
description: Phase 1. Read legacy documentation (files in 01-legacy/input/raw/ or an MCP source like Confluence/Jira/Drive), build an inventory, and extract cited Knowledge Units per process into 01-legacy/output/.
argument-hint: "<SPIKE-###>"
---
# Skill: ingest-legacy-docs
**Agent:** `doc-analyst` (delegate if your tool supports subagents)

## Inputs
- `04-audit/spikes/<SPIKE>/validation-process.md` (scope)
- `00-context/sources.md` rows with corpus = legacy
- `01-legacy/input/raw/**` and/or the MCP doc tools
- `00-context/domain-glossary.md`, `01-legacy/RULES.md`, `01-legacy/AGENTS.md`

## Preconditions
- The spike's validation process is approved (G0).
- At least one legacy source is reachable.

## Steps
1. Read `01-legacy/AGENTS.md` and `RULES.md`.
2. **Inventory:** enumerate the documents from each legacy source and fill `templates/inventory.md` → `01-legacy/output/inventory.md`. Mark processed/skipped with a reason (out of scope, duplicate, unreadable).
3. For each processed doc that is relevant to the in-scope process(es):
   - Extract Knowledge Units per `guide/03-knowledge-schema.md`. **One fact per KU.**
   - Cite `doc:<doc-id>#<section/page>` with an excerpt of ≤ 3 lines, plus the doc date.
   - Use domain glossary terms. Collect new candidate terms.
4. Detect contradictions between legacy docs. Link the KUs through `related:` and add a note.
5. Write `01-legacy/output/knowledge/<P-PROC>.md` from `templates/knowledge-unit.md` (banner 🟨, status `proposed`).
6. Run `/verify-citations 01-legacy/output/knowledge/<P-PROC>.md`.
7. Report: docs processed/skipped, KUs per type, L-confidence count, contradictions. Suggest `/review-gate 01-legacy`.

## Output
`01-legacy/output/inventory.md`, `01-legacy/output/knowledge/<P-PROC>.md`

## Human gate
G1: business SME (sample + flagged items).

## Common failures
- Scanned PDFs: request a text version, or run OCR outside the repo.
- Very long docs: process them by section and keep a section ID in the citations.
