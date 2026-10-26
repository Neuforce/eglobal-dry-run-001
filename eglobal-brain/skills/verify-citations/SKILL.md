---
name: verify-citations
description: Check that every Knowledge Unit, discrepancy or requirement in a file has a resolvable source citation and an excerpt that matches the source; flag unsupported claims.
argument-hint: "<path-to-file-or-folder>"
---
# Skill: verify-citations
**Agent:** `verifier`

## Steps
1. Parse the items (KU-, DISC-, REQ-, VR-) in the target.
2. For each item: does it have a `source`? Is the format valid (`AGENTS.md` §6)? Does it have an excerpt (KUs)?
3. Resolve a sample (all of them if fewer than 30; otherwise 30 + all the L-confidence ones): open the doc section or code lines and check that the excerpt is really there and supports the statement.
4. Mark the failures: `status: needs-source`, with a note. Never delete content.
5. Report: total, missing citation, malformed, excerpt mismatch, statement not supported.
