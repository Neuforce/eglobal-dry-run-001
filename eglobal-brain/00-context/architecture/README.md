# Architecture Inputs

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Why this folder matters
The PoCs (Phase 6) and the SDD design (Phase 5b) must respect eGlobal's real architecture: platform, standards, integrations, and NFRs. **We have not seen eGlobal's architecture yet**, so almost everything here is 🟥 REQUIRED.

`/plan-poc` **refuses to run** while any file in this folder is still 🟥.

## Files
| File | Status | What is needed | Minimum to unblock a PoC |
|---|---|---|---|
| `current-architecture.md` | 🟥 | Systems, components, data flows of today | C4 level 1 (context) for the in-scope processes |
| `target-architecture.md` | 🟥 | To-Be principles and reference architecture | Principles + target runtime style |
| `platform-openshift.md` | 🟥 | Cluster/namespace, images, registry, build, routes, secrets, quotas | Namespace + base image + build method |
| `standards.md` | 🟥 | Languages, frameworks, API style, logging, testing | Language/framework + API style |
| `integration-catalog.md` | 🟥 | Systems the processes talk to, protocols, contracts | Integrations of the PoC slice + whether mocks are acceptable |
| `nfrs.md` | 🟥 | Performance, availability, security, compliance | The NFRs the PoC must demonstrate |
| `adr/` | 🟨/🟩 | Architecture decisions | — |

Tip: if a full answer isn't available, fill the **minimum** column and mark the rest `TBD`. Then change the banner to 🟨 (partially provided) and note what's missing.
