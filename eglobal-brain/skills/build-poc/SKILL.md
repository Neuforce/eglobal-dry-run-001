---
name: build-poc
description: Phase 6b. Scaffold and build an approved PoC — source, Containerfile, OpenShift manifests, mocks, acceptance tests — following eGlobal standards; run it locally and validate manifests.
argument-hint: "<POC-###-slug>"
---
# Skill: build-poc
**Agent:** `poc-engineer`

## Inputs
- `06-poc/<POC>/poc-plan.md` (approved), `05-spec/<CAP>/sdd.md`, `05-spec/<CAP>/AGENTS.md`
- `00-context/architecture/standards.md`, `platform-openshift.md`, `integration-catalog.md`

## Preconditions
- The PoC plan is approved. The architecture has no 🟥 files.

## Steps
1. Scaffold the folder layout from `06-poc/AGENTS.md`.
2. Implement only the REQs in the slice. Follow `standards.md` (language, logging, error handling).
3. Build the mocks in `mocks/` from the integration contracts.
4. Write the acceptance tests in `tests/`, named after their REQ/AC IDs.
5. Write the `Containerfile` (approved base image, non-root, minimal layers).
6. Write `openshift/` manifests (Deployment, Service, Route, ConfigMap, with resource requests/limits and probes).
7. Build and run locally (docker). Run the tests. Validate the manifests with `oc apply --dry-run=client -f openshift/` (or kubectl).
8. Write `README.md` (build/run/deploy). **Ask before** any deploy to a shared cluster.
9. Record the results and any deviation, for `poc-findings`.

## Human gate
The Tech Lead reviews the code. The Architect reviews deviations in findings.
