# PRD: CAP-001-reverso-timeout Reverso por timeout del emisor

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

- **Version:** 0.1 · **Date:** 2026-10-24 · **Owner:** dry-run
- **Based on:** validated-asis/P-REV.md v1.0, audit-report findings #1

## 1. Problem and context
Los tres relatos del timeout no coinciden. El que corre es el de 25 segundos, fijo en el código. El To-Be de este slice lo hace configurable por emisor sin perder ese valor por defecto.

## 2. Users and actors
Adquirente, switch, emisor.

## 3. Goals / non-goals
| Goal | Metric | Source |
|---|---|---|
| G1 Timeout por emisor, default 25 s | AC-001.1 y AC-001.2 en verde | VR-REV del timeout, hallazgo 1 |
| Fuera de meta | Cola manual y reintentos | DISC-REV-002, DISC-REV-003 |

## 4. Scope
| Item | Change (new / modified / retired / unchanged) | As-Is ref |
|---|---|---|
| Timeout | modified | VR del timeout, decisión D-001 |
| Destino del reverso | unchanged | VR del reverso al adquirente |
| Lista de emisores | unchanged | VR de emisor autorizado |
| Cola manual | retired en este slice | DISC-REV-002 |
| Reintentos | unchanged, no entra al slice | DISC-REV-003 |

## 5. User journeys / scenarios
1. El emisor A tiene timeout de 20 s y no responde: hay reverso al adquirente.
2. Un emisor sin configuración no responde en 25 s: hay reverso.
3. El emisor responde a tiempo: no hay reverso.

## 6. Business rules carried over / changed
| VR / KU ref | As-Is rule | To-Be rule | Change |
|---|---|---|---|
| D-001 / KU-ASIS-REV timeout | 30 segundos, redacción de intención | Timeout por emisor, default 25 s | modified |
| KU-ASIS-REV reverso | El reverso va al adquirente | Igual | unchanged |

## 7. Success metrics
Las dos AC del timeout pasan en local.

## 8. Constraints and assumptions
Dos contenedores, emisor simulado, datos sintéticos. Imagen base real de eGlobal: desconocida.

## 9. Risks and open questions
El proceso es ficticio. Un despliegue en el clúster de eGlobal no está hecho.

## 10. Approval
Omitida en dry-run 001.
