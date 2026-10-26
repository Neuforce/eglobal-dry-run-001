# DISC-REV-003: timeout

- **Category:** ⚠️ Drift
- **Process / step:** P-REV / 3. Esperar respuesta del emisor
- **Impact:** M. Cambia el comportamiento del reverso o deja una regla sin respaldo.

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## Evidence
| Source | KU | Says | Citation |
|---|---|---|---|
| Legacy | KU-LEG-REV-002 | Cuando el emisor no responde en 45 segundos, el sistema genera un reverso automático hacia el adquirente. | doc:LEG-REV-proceso-reverso.md#3.2 |
| As-Is | KU-ASIS-REV-003 | Cuando el emisor no responde en 30 segundos, el sistema genera un reverso automático hacia el adquirente. | doc:ASIS-REV-proceso-reverso.md#3.2 |
| Code | KU-CODE-REV-003 | Cuando el emisor no responde en 25 segundos, el sistema genera un reverso automático hacia el adquirente. | code:legacy-readonly/switch_core/reversal.py:40@dry-run-001 |

## Analysis (agent)
Las fuentes de este `match` no cuentan la misma regla, o la regla vive en un solo lado.

## Recommendation (agent, non-binding)
El To-Be deja el timeout configurable por emisor; el valor por defecto sale del código (25 s).

## Decision (dry-run, no humana)
- **Decision:** code is right
- **Truth statement:** Cuando el emisor no responde en 25 segundos, el sistema genera un reverso automático hacia el adquirente.
- **Follow-up:** El To-Be deja el timeout configurable por emisor; el valor por defecto sale del código (25 s).
- **Decided by:** dry-run 001 automático · **Date:** 2026-10-24 · **Ref:** decision:04-audit/review/decision-log.md#D-003
