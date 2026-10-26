# Open Questions / Blind Spots

> **🟥 REQUIRED — eGlobal input needed.** We do not have enough information to infer this. **Owner:** Tech Lead + Alejandra (answers) · **Blocks:** Phase 0

<!--
PURPOSE:     Questions NeuForce or the agents can't answer. Each answer may change a 🟨 assumption or fill a 🟥 file.
HOW TO FILL: Answer inline, then move the item to "Resolved" with who/when.
-->

## Open
| # | Question | Why it matters | Hypothesis | Affects | Owner | Answer |
|---|---|---|---|---|---|---|
| Q1 | How is the As-Is documented today (tool, format, granularity, sign-off)? | Defines Phase 2 ingestion | Word/Confluence docs per process | `sources.md`, Phase 2 | Alejandra | |
| Q2 | Where does the legacy documentation live? MCP access or export only? | Defines Phase 1 access | Confluence/Jira + files | `sources.md`, `.mcp.json` | Tech Lead | |
| Q3 | Which repos, languages, and branches implement the in-scope processes? Is there a module ↔ process map? | Defines Phase 3 | Several repos, no explicit map | `repos.md` | Tech Lead | |
| Q4 | Which LLM tools are approved internally (Gemini Enterprise, Cognition/Devin, others)? Are MCP servers allowed? | Tool setup | Gemini Enterprise approved | `guide/04-tool-setup.md` | Tech Lead / Security | |
| Q5 | Is an OpenShift sandbox/namespace available for PoCs? Who administers it? | Phase 6 | Yes, dev namespace | `architecture/platform-openshift.md` | Architect | |
| Q6 | Are there architecture standards or reference docs for the To-Be? | Phase 5b/6 | Partially exist | `architecture/*` | Architect | |
| Q7 | Any compliance/regulatory limits on what an LLM may read (e.g. PCI scope)? | Security | Code OK, no prod data | `guide/05-security.md` | Security | |
| Q8 | Which process should SPIKE-001 cover? | First spike | TBD | `process-inventory.md` | Alejandra | |
| Q9 | Should generated docs be in Spanish? | Output language | Yes (Spanish), IDs in English | `AGENTS.md` §9 | PM | |
| Q10 | Who are the gate approvers (Tech Lead, Architect, business owner, SMEs)? | HITL | TBD | `stakeholders.md` | PM | |

## Resolved
| # | Answer | By | Date |
|---|---|---|---|
