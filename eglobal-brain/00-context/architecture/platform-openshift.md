# Platform: OpenShift

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

| Item | Value |
|---|---|
| OpenShift version | no provisto; el dry run no despliega |
| Cluster / environment for PoCs | local (Podman o Docker), mismos Containerfile |
| Namespace / project | dry-run-001 |
| Who can deploy (service account, RBAC) | nadie en este corrido |
| Approved base images (UBI? versions) | no provisto; el PoC usa `python:3.12-slim` y lo anota como desviación |
| Image registry | local |
| Build method (S2I / Containerfile + pipeline / local build + push) | Containerfile |
| CI/CD (Tekton/OpenShift Pipelines, ArgoCD/GitOps, Jenkins, GitHub Actions) | no |
| Ingress (Routes, TLS policy) | Route de ejemplo, sin TLS |
| Secrets management (Secrets, Vault, Sealed Secrets) | Secret de ejemplo, valor ficticio |
| Config (ConfigMaps conventions) | ConfigMap `poc-001-reverso-config` |
| Resource quotas / limits per pod | requests 50m/64Mi, limits 200m/128Mi |
| Network policies / egress restrictions | no definidas |
| Observability (logging, metrics, tracing stack) | stdout |
| Security context constraints (non-root, etc.) | runAsNonRoot, uid 10001 |

## Local alternative
El dry run corre las pruebas en el intérprete local. Los manifiestos quedan escritos para `oc apply --dry-run=client` cuando haya `oc`.
