# DISC-REV-002: reintentos

- **Category:** 🕳️ Undocumented
- **Process / step:** P-REV / 3. Esperar respuesta del emisor
- **Impact:** M. Cambia el comportamiento del reverso o deja una regla sin respaldo.

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## Evidence
| Source | KU | Says | Citation |
|---|---|---|---|
| Legacy | — | — | — |
| As-Is | — | — | — |
| Code | KU-CODE-REV-004 | Cuando el emisor no responde, el sistema reintenta la consulta hasta 3 veces antes de disparar el reverso. | code:legacy-readonly/switch_core/reversal.py:52@dry-run-001 |

## Analysis (agent)
Las fuentes de este `match` no cuentan la misma regla, o la regla vive en un solo lado.

## Recommendation (agent, non-binding)
Está en el código y no en los documentos. No se promueve a regla validada en este dry run.

## Decision (dry-run, no humana)
- **Decision:** needs investigation
- **Truth statement:** —
- **Follow-up:** Está en el código y no en los documentos. No se promueve a regla validada en este dry run.
- **Decided by:** dry-run 001 automático · **Date:** 2026-10-24 · **Ref:** decision:04-audit/review/decision-log.md#D-002
