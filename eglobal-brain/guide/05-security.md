# Security and Data Handling

> **🟨 ASSUMPTION — review & approve.** Pre-filled by NeuForce from kickoff conversations (2026-10-05). Correct anything wrong, then mark approved. **Approver:** eGlobal Security / Tech Lead · **Blocks:** Step 0

## Assumptions in this file
- A1. NeuForce does **not** get access to eGlobal code repositories. Code is read only by the agent running on eGlobal's side.
- A2. NeuForce may get **read-only** access to this brain repo (fork or shared).
- A3. The LLM tools used are approved by eGlobal for internal (non-public) data.
- A4. No customer PII or card data is needed in this repo. Rules are described, not data.

## Rules
1. **Read-only code access.** The GitHub MCP runs with `--read-only` and a fine-grained token scoped to the in-scope repos.
2. **No code copying.** Cite `repo/path:line` with excerpts of ≤ 3 lines. PoC code is new code, written from the spec.
3. **No secrets in git.** `.mcp.json`, `.env`, and tokens are git-ignored. Use environment variables.
4. **No production data.** PoCs use synthetic or mocked data only.
5. **Data classification.** If a raw document is classified above "internal", do not place it in `input/raw/`. Summarize it manually or connect through an approved MCP that respects permissions.
6. **Human approval for anything outward-facing.** Pushes, deployments to shared clusters, and sharing the repo all need explicit human approval (see `.claude/settings.json`).

## Open items for eGlobal Security
- [ ] Approved LLM tools and tenants
- [ ] MCP servers allowed (local Docker / remote)
- [ ] Classification of the legacy and As-Is docs
- [ ] OpenShift namespace and policy for PoCs
