# AGENTS.md — eGlobal Brain (global instructions)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

You are working in the **eGlobal Brain repo**: the single source of truth for discovering, validating, and specifying the eGlobal system, and for prototyping its To-Be. This repo holds **knowledge and process**. It does **not** hold production code. Production code lives in eGlobal's repositories and is read **only** through the GitHub MCP, in read-only mode.

These instructions work with any agent (Claude Code, Gemini CLI / Gemini Enterprise, Codex, Devin). `CLAUDE.md` and `GEMINI.md` only import this file.

## 1. Mission
1. Turn three sources (legacy docs, new As-Is docs, code) into one **validated As-Is**.
2. Turn the validated As-Is into a **To-Be spec** (PRD → SDD + per-subprocess `AGENTS.md`).
3. Turn the spec plus the architecture template into **PoCs** on OpenShift, with documented findings.

The goal is not only the spec. It is the **instrumentation of the whole process**: every phase leaves reusable artifacts, rules, and agent instructions.

## 2. Repo map
| Path | What it is | Who writes |
|---|---|---|
| `guide/` | How the method works, the prompt guide, policies | NeuForce |
| `00-context/` | Project inputs: scope, stakeholders, sources, repos, architecture | **eGlobal humans** |
| `01-legacy/` | Phase 1: legacy docs → Knowledge Units | Agent + SME review |
| `02-asis/` | Phase 2: new As-Is docs → Knowledge Units + delta vs legacy | Agent + Alejandra review |
| `03-code/` | Phase 3: code → Knowledge Units (via GitHub MCP) | Agent + Tech Lead review |
| `04-audit/` | Phase 4: cross-reference → discrepancies → **validated As-Is** | Agent + joint review |
| `05-spec/` | Phase 5: PRD, SDD, subprocess AGENTS.md | Agent + business/tech review |
| `06-poc/` | Phase 6: containerized PoCs + findings | Agent + Architect review |
| `templates/` | Blank templates. **Always** copy from here; never invent a format | NeuForce |
| `skills/` | Executable procedures (one per step) | NeuForce |
| `agents/` | Subagent role definitions | NeuForce |
| `decisions/` | Approvals and decision log | Humans |
| `examples/` | A fictional, fully worked example of what "good" looks like | NeuForce |

## 3. Before you do anything in a phase folder
1. Read that folder's `AGENTS.md` (phase scope and done-criteria).
2. Read that folder's `RULES.md` (rules learned from human corrections). **These rules override your defaults.**
3. Check the preconditions in the skill you are running. If one fails, stop and tell the user exactly what is missing.

## 4. Phase order and gates
`0 Setup → 1 Legacy → 2 As-Is → 3 Code → 4 Audit → 5 Spec → 6 PoC`
- Phases 1, 2 and 3 can run in parallel once Phase 0 is approved.
- Phase 4 needs approved outputs from 1, 2 and 3 for the processes in scope.
- Phase 6 is **blocked** until `00-context/architecture/` has no 🟥 REQUIRED files left.
- A phase is "done" only when its gate is approved by a human and recorded in its `review/` log.

## 5. File status banners
Every human-facing file starts with one banner:
- `🟥 REQUIRED`: eGlobal must provide this. **Never invent content for these files.** You may help a human fill one by interviewing them (`/setup-context`).
- `🟨 ASSUMPTION`: pre-filled by NeuForce. Treat it as provisional and mention the assumption when you rely on it.
- `🟩 METHOD`: NeuForce standard.
- `✅ APPROVED`: a human approved it. **Only humans set this banner. Never set it yourself.**

## 6. Citation policy (non-negotiable)
- Every Knowledge Unit (KU), discrepancy, and spec requirement must trace to a source.
  - Documents: `doc:<file-or-page-id>#<section-or-page>`
  - Code: `code:<repo>/<path>:<line-start>-<line-end>@<branch-or-sha>`
  - Human decision: `decision:<log-file>#<entry-id>`
- A short verbatim excerpt (≤ 3 lines) goes with each citation. Never paste large code blocks.
- If you cannot cite it, mark it `confidence: L` and `status: needs-source`. Do not present it as fact.

## 7. Human-in-the-loop policy
- You **propose**. Humans **approve, correct, or reject**.
- Never resolve a ❓ Ambiguous or ⚠️ Drift item yourself. Present the evidence and a recommendation.
- When a human corrects you, run `/review-gate` so the correction becomes an `R-###` rule in that phase's `RULES.md`.

## 8. IDs and naming
| Item | Format | Example |
|---|---|---|
| Process | `P-<SHORT>` (from `00-context/process-inventory.md`) | `P-CONC` |
| Knowledge Unit | `KU-<LEG\|ASIS\|CODE>-<PROC>-<###>` | `KU-CODE-CONC-014` |
| Discrepancy | `DISC-<PROC>-<###>` | `DISC-CONC-003` |
| Rule | `R-<phase#>-<###>` | `R-3-007` |
| Spike | `SPIKE-<###>` | `SPIKE-001` |
| Capability (spec) | `CAP-<###>-<slug>` | `CAP-001-conciliacion` |
| PoC | `POC-<###>-<slug>` | `POC-001-conciliacion-batch` |
- File names: kebab-case. One process per knowledge file: `knowledge/<process-id>.md`.

## 9. Language
- Generated documents are written in **Spanish**. IDs, field names, and file names stay in **English**. (🟨 Assumption, see `README.md`.)

## 10. Security
- Read-only access to code. Never commit secrets, tokens, or `.mcp.json`.
- Never copy production code into this repo. Cite it instead. PoC code is new code written from the spec.
- Do not send repo content to any external service except the LLM/MCP tools configured by eGlobal.
- See `guide/05-security.md`.

## 11. When unsure
Stop and ask. Add the question to `00-context/open-questions.md` with your best hypothesis.
