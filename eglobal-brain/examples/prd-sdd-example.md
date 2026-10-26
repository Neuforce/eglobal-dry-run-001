## PRD row
| VR / KU ref | As-Is rule | To-Be rule | Change |
|---|---|---|---|
| VR-EX-003 | Global timeout 25 s | Timeout configurable per issuer, default 25 s | modified |

## SDD requirement
### REQ-004 Timeout de reverso configurable por emisor
- **EARS:** Cuando el emisor no responde dentro del timeout configurado para ese emisor, el sistema deberá generar un reverso automático.
- **Source:** VR-EX-003, PRD goal G2
- **Change:** modified
- **Acceptance criteria:**
  - [ ] AC-004.1 Given emisor A con timeout 20 s, when no responde en 20 s, then se genera un reverso.
  - [ ] AC-004.2 Given un emisor sin configuración, when no responde en 25 s, then se genera un reverso (default).
