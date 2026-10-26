# Tool Setup

> **🟨 ASSUMPTION — review & approve.** Pre-filled by NeuForce from kickoff conversations (2026-10-05). Correct anything wrong, then mark approved. **Approver:** Tech Lead · **Blocks:** Step 0

## Assumptions in this file
- A1. eGlobal's Tech Lead uses an approved internal LLM tool, likely **Gemini Enterprise** and/or **Cognition (Devin)**. Claude Code also works.
- A2. Running MCP servers locally (Docker) or connecting to remote MCP endpoints is allowed by eGlobal security.
- A3. Legacy docs are in Atlassian (Confluence/Jira) and/or Google Drive/SharePoint, or exportable as files.
- A4. A read-only GitHub Personal Access Token (fine-grained, `Contents: read`, `Metadata: read`) can be issued for the in-scope repos.

## 1. Clone
```bash
git clone <eglobal-brain-url> && cd eglobal-brain
```
Windows: run `git config core.symlinks true` before cloning (`.claude/skills` and `.claude/agents` are symlinks).

## 2. MCP connectors
```bash
cp .mcp.example.json .mcp.json   # .mcp.json is git-ignored
export GITHUB_PAT_READONLY=<fine-grained read-only token>
```
- **GitHub:** the official `github/github-mcp-server`, run with `--read-only` and only the `repos` toolset.
- **Atlassian (Confluence/Jira):** Atlassian's remote MCP server. Check the current endpoint in Atlassian's docs before use. Authenticate with OAuth in the browser.
- **Google Drive / SharePoint:** use the connector approved in your tenant (Gemini Enterprise has native Drive connectors). If no connector is allowed, export the files to `01-legacy/input/raw/` or `02-asis/input/raw/`.

## 3. Per tool
| Tool | Instructions file | Skills | MCP config |
|---|---|---|---|
| Claude Code | `CLAUDE.md` → imports `AGENTS.md` | `/skill-name` (from `.claude/skills`) | `.mcp.json` |
| Gemini CLI | `GEMINI.md` → imports `AGENTS.md` | "Follow skills/<name>/SKILL.md" | `.gemini/settings.json` → `mcpServers` (same shape) |
| Gemini Enterprise | Upload or connect the repo; point the agent to `AGENTS.md` | "Follow skills/<name>/SKILL.md" | Tenant connectors |
| Codex | Reads `AGENTS.md` natively | "Follow skills/<name>/SKILL.md" | `~/.codex/config.toml` |
| Devin | Add `AGENTS.md` as a knowledge/playbook entry | Playbook per skill | Devin integrations |

## 4. Smoke test
Ask the agent:
1. `Read AGENTS.md and summarize the phases.`
2. `List files in <one in-scope repo> using the GitHub MCP.`
3. `List the documents you can access in <doc source>.`
