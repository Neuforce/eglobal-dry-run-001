# ADR-001: PoC approach (OpenShift, 1–2 containers, mocked integrations)

> **🟨 ASSUMPTION — review & approve.** Pre-filled by NeuForce from kickoff conversations (2026-10-05). Correct anything wrong, then mark approved. **Approver:** Architect · **Blocks:** Phase 6

- **Status:** proposed
- **Date:** 2026-10-06
- **Deciders:** TBD (eGlobal Architect), NeuForce

## Context
We need to show quickly that spec'd capabilities can run on eGlobal's platform, without access to production systems, before construction starts in about 2 months.

## Decision
- PoCs run on **OpenShift**, or locally with Podman when no cluster is available, using the same Containerfile.
- Each PoC is **1–2 containers** with a minimal architecture slice.
- External integrations are **mocked** from the contracts in `integration-catalog.md`.
- Only **synthetic data**.
- Each PoC is timeboxed and ends with `findings.md`: worked / didn't work / considerations / go-pivot-drop.

## Consequences
- Fast, low-risk feedback on feasibility and design.
- PoCs do not prove production integration or performance at scale. Those go into the findings as follow-ups.

## Alternatives considered
- Prototype directly against eGlobal environments: rejected, because it needs access we don't have and adds risk.
