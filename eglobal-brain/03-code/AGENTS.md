# AGENTS.md — 03-code (Phase 3: rules from code via GitHub MCP)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Goal
Extract what the **code actually does** for the in-scope processes, as cited KUs, plus a code map.

## Inputs
- `00-context/repos.md` (repos, branch, module ↔ process mapping, exclusions)
- GitHub MCP (read-only)
- Spike scope (`validation-process.md`): strategy docs→code or code→docs
- For docs→code: `02-asis/output/knowledge/` (what to look for)

## Outputs
- `output/code-map.md`: entry points → call chain → key classes/functions/tables per process
- `output/knowledge/<P-PROC>.md`: KUs with `code:` citations

## Rules
- Read `RULES.md` first.
- **Read-only.** Never open PRs or issues, or modify the repos.
- **Cite, don't copy.** Citation `code:<repo>/<path>:<start>-<end>@<sha>` + an excerpt of ≤ 3 lines.
- Write statements in **business language** ("When the amount exceeds X, the transaction is rejected"), not code language.
- Capture constants, thresholds, and config values with their source (code, config file, DB). If a value comes from runtime config you can't see, say so (`confidence: M`).
- Note dead or unreachable code when you see it. It often explains 👻 Orphan items.
- Respect the exclusions in `repos.md`.

## Done-criteria (G3)
- Every in-scope process has a code map and KUs.
- The Tech Lead verifies a sample of citations (they resolve and are interpreted correctly).
