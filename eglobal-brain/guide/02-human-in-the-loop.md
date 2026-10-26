# Human-in-the-Loop Protocol

> **🟨 ASSUMPTION — review & approve.** Pre-filled by NeuForce from kickoff conversations (2026-10-05). Correct anything wrong, then mark approved. **Approver:** eGlobal PM + Tech Lead · **Blocks:** all gates

## Assumptions in this file
- A1. Alejandra owns the As-Is and approves business-side gates.
- A2. A single Tech Lead (name TBD) owns the repo and approves code-side gates.
- A3. The sampling rate for reviewing Knowledge Units is **20%, with a minimum of 10 KUs per process**. Every ⚠️ / ❓ / L-confidence item is always reviewed.
- A4. Gates are reviewed in the weekly Wednesday working session, or asynchronously through a PR.

## The loop
```
Agent proposes ─► review packet ─► Human: ✅ approve | ✏️ correct | ❌ reject
      ▲                                              │
      └──────── RULES.md updated (R-###) ◄───────────┘
```

## RACI per gate
| Gate | Responsible (prepares) | Approves | Consulted |
|---|---|---|---|
| G0 Context ready + spike design | Tech Lead | Alejandra + Tech Lead | NeuForce |
| G1 Legacy KUs | Agent + Tech Lead | Business SME (TBD) | Alejandra |
| G2 As-Is KUs | Agent | Alejandra | SMEs |
| G3 Code KUs | Agent | Tech Lead | Developers |
| G4 Discrepancies + validated As-Is | Agent + NeuForce | Alejandra **and** Tech Lead | SMEs |
| G5a PRD | Agent | Business owner / eGlobal PM (TBD) | Alejandra |
| G5b SDD | Agent | Tech Lead / Architect (TBD) | NeuForce |
| G6 PoC plan + findings | Agent | Architect (TBD) | Tech Lead |

## How to review
1. Run `/review-gate <phase-folder>`. You get a review packet: the sample, every flagged item, and the evidence.
2. For each item, answer **approve**, **correct: <what is right>**, or **reject: <why>**.
3. The agent:
   - records the decisions in `<phase>/review/review-log.md`;
   - updates the affected files;
   - turns each correction into an `R-###` rule in `<phase>/RULES.md`, if it generalizes;
   - asks the approver to confirm the gate.
4. The approver changes the banner of the gated output to `✅ APPROVED` and adds a line to `decisions/approvals.md`.

## Acceptance thresholds (proposed)
- KU sample accuracy ≥ 90% before a gate can pass. Otherwise: add rules, re-run, re-sample.
- Every ⚠️ and ❓ item in scope has a decision before G4.
