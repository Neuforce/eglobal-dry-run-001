# Prompt Guide: Step by Step

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

Follow the steps in order. Each step tells you **who** runs it, **what to type**, **what you get**, **who approves it**, and **when it is done**.

**How to run a skill:**
- **Claude Code:** type `/<skill-name> <args>`
- **Gemini CLI / Gemini Enterprise / Codex / Devin:** type `Follow skills/<skill-name>/SKILL.md with args: <args>`

After any step that ends in a 🟧 gate, run `/review-gate <phase-folder>`. Do not move on until the owner approves.

---

### Step 0: Clone and set up tools
- **Who:** Tech Lead
- **Do:** Clone the repo. Copy `.mcp.example.json` to `.mcp.json`. Set the `GITHUB_PAT_READONLY` env var. Follow `guide/04-tool-setup.md` for your LLM tool.
- **Check:** Ask the agent `List the MCP tools you can use`. It should list the GitHub tools, plus the doc tools if configured.
- **Done when:** the agent can list one in-scope repo and one document source.

### Step 1: Fill the context
- **Who:** Tech Lead + Alejandra (about 60–90 minutes)
- **Run:** `/setup-context`
- **Expect:** The agent interviews you and fills the 🟥 files in `00-context/`. It ends with a readiness report.
- **Review:** Approve the 🟨 assumption files listed in `README.md` → *Review & Input Guide*.
- **Done when:** `scripts/review-status.sh` shows no 🟥 left in `00-context/` (architecture can wait until Step 11).

### Step 2: Design the validation process (first spike)
- **Who:** Tech Lead + Alejandra
- **Run:** `/design-validation-process SPIKE-001 P-<PROC>`
- **Expect:** `04-audit/spikes/SPIKE-001/validation-process.md` with the scope, the strategy (docs→code or code→docs), the steps, and the sampling plan.
- **🟧 Gate:** Alejandra + Tech Lead approve.
- **Done when:** approved and recorded in `04-audit/review/decision-log.md`.

### Step 3: Legacy documentation
- **Who:** Tech Lead (an SME reviews)
- **Run:** `/ingest-legacy-docs SPIKE-001`
- **Expect:** `01-legacy/output/inventory.md` and `01-legacy/output/knowledge/<P-PROC>.md`
- **🟧 Gate:** `/review-gate 01-legacy`. The SME reviews the sample.

### Step 4: New As-Is documentation
- **Run:** `/ingest-asis-docs SPIKE-001`
- **Expect:** `02-asis/output/knowledge/<P-PROC>.md` and `02-asis/output/legacy-delta.md`
- **🟧 Gate:** `/review-gate 02-asis`. Owner: Alejandra.

### Step 5: Code extraction
- **Run:** `/extract-code-rules SPIKE-001`
- **Expect:** `03-code/output/code-map.md` and `03-code/output/knowledge/<P-PROC>.md`
- **🟧 Gate:** `/review-gate 03-code`. Owner: Tech Lead.

### Step 6: Cross-reference
- **Run:** `/cross-reference SPIKE-001`
- **Expect:** `04-audit/output/traceability-matrix.csv` and `04-audit/output/discrepancies/DISC-*.md`

### Step 7: Joint gate session
- **Who:** Alejandra + Tech Lead (NeuForce facilitates)
- **Run:** `/review-gate 04-audit`
- **Do:** Resolve every ⚠️ and ❓. The agent records decisions in `04-audit/review/decision-log.md` and turns corrections into rules.

### Step 8: Audit report and validated As-Is
- **Run:** `/audit-report SPIKE-001`
- **Expect:** `04-audit/output/validated-asis/<P-PROC>.md` and `04-audit/output/audit-report.md`
- **🟧 Gate:** Alejandra + Tech Lead sign off.

### Step 9: PRD
- **Run:** `/write-prd CAP-001-<slug>`
- **Expect:** `05-spec/CAP-001-<slug>/prd.md`
- **🟧 Gate:** Business owner.

### Step 10: SDD and subprocess AGENTS.md
- **Run:** `/write-sdd CAP-001-<slug>`
- **Expect:** `sdd.md` and `AGENTS.md` in the capability folder
- **🟧 Gate:** Tech Lead / Architect.

### Step 11: Architecture readiness check
- **Run:** `scripts/review-status.sh 00-context/architecture`
- **Done when:** no 🟥 files are left. Otherwise, fill them first (`/setup-context architecture`).

### Step 12: PoC plan
- **Run:** `/plan-poc POC-001-<slug> CAP-001-<slug>`
- **🟧 Gate:** Architect.

### Step 13: Build the PoC
- **Run:** `/build-poc POC-001-<slug>`
- **Expect:** `06-poc/POC-001-<slug>/` with src, Containerfile, OpenShift manifests, and tests.

### Step 14: Findings and demo
- **Run:** `/poc-findings POC-001-<slug>`
- **Expect:** `findings.md` (worked / didn't work / considerations / go-pivot-drop)
- **🟧 Gate:** Architect, then the demo to Champions.

---

**Anytime:** run `/status` to see where you are, and `/verify-citations <path>` to check sources.
