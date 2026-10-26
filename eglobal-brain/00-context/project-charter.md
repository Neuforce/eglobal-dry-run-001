# Project Charter: eGlobal Discovery and Prototyping

> **🟨 ASSUMPTION — review & approve.** Pre-filled by NeuForce from kickoff conversations (2026-10-05). Correct anything wrong, then mark approved. **Approver:** eGlobal PM (Karina?) + Aníbal Abarca · **Blocks:** Phase 0

## Assumptions in this file
- A1. Construction of the real project starts in **about 2 months**. This engagement removes risk from it.
- A2. Horizon: **about 4 weeks**. The first half validates the As-Is, the second half writes the spec and starts prototypes.
- A3. PoCs run on **OpenShift**, in 1–2 containers, with a minimal architecture.
- A4. NeuForce does not need access to eGlobal systems. eGlobal runs the agents. NeuForce designs, facilitates, and reviews.
- A5. A Champions demo happens in **week 3**.
- A6. The weekly working session is on **Wednesdays**, with the working team only (no Champions).

## 1. Objectives
1. Produce a **validated As-Is** for the in-scope processes by cross-referencing legacy docs, the new As-Is docs, and code.
2. Produce a **To-Be spec** (PRD + SDD) for the first prioritized capability.
3. Build at least **one PoC** on OpenShift and document what worked, what didn't, and what to consider.
4. Leave eGlobal with a **reusable, agent-ready repo and method** (skills, rules, templates) that the team can run on its own.

## 2. Scope
| In scope | Out of scope |
|---|---|
| As-Is processes listed in `process-inventory.md` | Production development |
| Read-only analysis of in-scope repos | Changes to eGlobal production repos |
| PoCs with mocked integrations | Integration with production systems/data |
| <!-- FILL: add / correct --> | <!-- FILL --> |

## 3. Timeline (proposed)
| Week | Focus | Milestone |
|---|---|---|
| 1 | Setup, context, SPIKE-001 design, start of Phases 1–3 | G0 approved |
| 2 | Phases 1–3 complete, cross-reference, audit | G4: validated As-Is (spike 1) |
| 3 | PRD + SDD, PoC plan | **Champions demo** |
| 4 | PoC build + findings | Findings review, plan for next spikes |

## 4. Success criteria
- [ ] ≥ 1 process with a validated As-Is signed off by Alejandra + Tech Lead
- [ ] Audit report showing coverage % and discrepancy breakdown
- [ ] Approved PRD + SDD for ≥ 1 capability
- [ ] ≥ 1 PoC running on OpenShift, with findings
- [ ] eGlobal team runs at least one phase without NeuForce driving

## 5. Cadence
- **Wednesday working session:** this team. Review the last gate, run the next step together.
- **Weekly PM sync:** Aníbal ↔ eGlobal PM.
- **Week 3:** Champions demo. Separate progress updates to leadership.
