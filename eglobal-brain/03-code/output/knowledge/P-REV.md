# Knowledge: P-REV Reverso por timeout del emisor (code)

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

- **Spike:** SPIKE-001
- **Generated:** 2026-10-24 by run-dry-run-001.py
- **Sources processed:** legacy-readonly/switch_core/reversal.py@dry-run-001

## Summary
El código usa 25 segundos, envía el reverso al adquirente, filtra emisores autorizados y reintenta hasta 3 veces. Ese reintento no está en los documentos.

## Knowledge Units

### KU-CODE-REV-001
- **step:** 1. Validar al emisor
- **type:** authorization
- **statement:** Cuando el emisor no está en la lista de emisores autorizados, el sistema rechaza la transacción antes de enviarla.
- **source:** code:legacy-readonly/switch_core/reversal.py:10@dry-run-001
- **excerpt:**
  > if emisor_id not in EMISORES_AUTORIZADOS:
- **confidence:** H
- **status:** proposed
- **glossary_terms:** emisor, autorizacion
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-CODE-REV-002
- **step:** 2. Enviar el reverso
- **type:** routing
- **statement:** Cuando se dispara un reverso, el sistema lo envía al adquirente.
- **source:** code:legacy-readonly/switch_core/reversal.py:28@dry-run-001
- **excerpt:**
  > DESTINO_REVERSO = "adquirente"
- **confidence:** H
- **status:** proposed
- **glossary_terms:** reverso, adquirente
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-CODE-REV-003
- **step:** 3. Esperar respuesta del emisor
- **type:** timing/SLA
- **statement:** Cuando el emisor no responde en 25 segundos, el sistema genera un reverso automático hacia el adquirente.
- **source:** code:legacy-readonly/switch_core/reversal.py:40@dry-run-001
- **excerpt:**
  > ISSUER_TIMEOUT_S = 25
- **confidence:** H
- **status:** proposed
- **glossary_terms:** reverso, emisor, adquirente, timeout
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-CODE-REV-004
- **step:** 3. Esperar respuesta del emisor
- **type:** exception-handling
- **statement:** Cuando el emisor no responde, el sistema reintenta la consulta hasta 3 veces antes de disparar el reverso.
- **source:** code:legacy-readonly/switch_core/reversal.py:52@dry-run-001
- **excerpt:**
  > MAX_REINTENTOS = 3
- **confidence:** H
- **status:** proposed
- **glossary_terms:** reverso, emisor, reintento
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24
