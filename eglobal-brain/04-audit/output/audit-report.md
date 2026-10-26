# Audit Report: As-Is Validation (SPIKE-001)

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## 1. Executive summary
- Alcance: un proceso ficticio, P-REV.
- El As-Is y el código coinciden en el destino del reverso y en la lista de emisores.
- El timeout no coincide: legacy 45 s, As-Is 30 s, código 25 s. El dry run se queda con el código.
- Hay una cola manual solo en el As-Is y un reintento de 3 veces solo en el código.
- El slice del PoC cubre el timeout configurable, con 25 s de valor por defecto.

## 2. Scope and method
- Processes: P-REV
- Sources: LEG-REV-proceso-reverso, ASIS-REV-proceso-reverso
- Repo: dry-run-legacy@dry-run-001
- Strategy: docs→code
- Gates held: ninguna. Las resolvió `run-dry-run-001.py`.

## 3. Coverage metrics
| Process | KUs legacy | KUs as-is | KUs code | ✅ | ⚠️ | 🕳️ | 👻 | ❓ | % As-Is in code | % code documented |
|---|---|---|---|---|---|---|---|---|---|---|
| P-REV | 2 | 4 | 4 | 2 | 1 | 1 | 1 | 0 | 75% | 75% |

## 4. Key findings
| # | Finding | DISC refs | Impact | Recommendation |
|---|---|---|---|---|
| 1 | El timeout documentado no es el que ejecuta el código | DISC-REV-001 | M | Spec: timeout por emisor, default 25 s |
| 2 | La cola manual no está en el código | DISC-REV-002 | M | Fuera de este slice |
| 3 | El código reintenta 3 veces y nadie lo documentó | DISC-REV-003 | M | Investigar en un spike posterior |

## 5. Risk heatmap
Un solo proceso, impacto medio, sin datos reales.

## 6. Recommendations for the To-Be
Hacer configurable el timeout por emisor. No integrar el emisor real en el PoC.

## 7. Method retrospective
- Reglas nuevas de fase: 0. Este corrido no escribe en `RULES.md`.
- Muestra humana: no hubo.
- Tiempo: un script, no una estimación manual.

## 8. Appendix: decision log summary
D-001 código manda en el timeout. D-002 cola manual fuera de alcance. D-003 reintentos sin promover.
