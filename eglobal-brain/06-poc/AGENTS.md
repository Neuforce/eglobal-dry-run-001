# AGENTS.md — 06-poc (Phase 6: prototypes)

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Goal
Build minimal, containerized PoCs from an approved SDD that respect eGlobal's architecture, and document what was learned.

## Precondition (hard)
- **No 🟥 files left in `00-context/architecture/`** (check with `scripts/review-status.sh 00-context/architecture`). If any are left, STOP and tell the user which ones.
- The SDD for the capability is approved (G5b).

## Folder layout
```
06-poc/POC-###-<slug>/
  poc-plan.md      (templates/poc-plan.md)
  src/
  Containerfile
  openshift/       deployment.yaml, service.yaml, route.yaml, configmap.yaml
  mocks/           mock integrations built from integration-catalog contracts
  tests/           acceptance tests derived from sdd.md
  findings.md      (templates/poc-findings.md)
  README.md        how to build/run locally and on OpenShift
```

## Rules
- Read `RULES.md` first.
- Follow `00-context/architecture/standards.md` and `platform-openshift.md` exactly: base images, non-root, resource limits, config through ConfigMaps, secrets through Secrets.
- 1–2 containers. Mock external systems. Synthetic data only.
- Acceptance tests come from the SDD acceptance criteria and reference the requirement IDs.
- Never deploy to a shared cluster without explicit human approval.
- Record every deviation from the architecture in `findings.md` with the reason.

## Done-criteria (G6)
- The PoC builds and runs (locally at minimum). Manifests validate.
- Acceptance tests run, with results recorded.
- `findings.md` complete and approved by the Architect.
