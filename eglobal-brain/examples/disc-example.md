# DISC-EX-002: Timeout before an automatic reversal: 30 s (doc) vs 25 s (code)

- **Category:** ⚠️ Drift
- **Process / step:** P-EX / 3. Esperar respuesta del emisor
- **Impact:** H. Affects when customers see reversals, and reconciliation.

## Evidence
| Source | KU | Says | Citation |
|---|---|---|---|
| Legacy | KU-LEG-EX-007 | 25 s | doc:LEG-Manual-Switch-v3.pdf#p41 |
| As-Is | KU-ASIS-EX-004 | 30 s | doc:ASIS-EX-Proceso-Reversos.docx#3.2 |
| Code | KU-CODE-EX-011 | 25 s default, configurable | code:example-org/switch-core/…/ReversalScheduler.java:42-44@a1b2c3d |

## Analysis (agent)
The code agrees with legacy (25 s). The As-Is says 30 s, which may reflect a production config override or a planned change.

## Recommendation (agent, non-binding)
Check the production value of `issuer.timeout.ms`. If it is 25 s, correct the As-Is doc.

## Decision (humans)
- **Decision:** code is right. Production config = 25 s (confirmed by the Tech Lead from the config repo).
- **Truth statement:** Cuando el emisor no responde en 25 s, el switch genera un reverso automático.
- **Follow-up:** Update the As-Is doc §3.2. In the To-Be, make the timeout configurable per issuer (backlog).
- **Decided by:** Alejandra + Tech Lead (ejemplo) · **Date:** 2026-10-15 · **Ref:** decision-log#2026-10-15-01
