# Knowledge: P-REV Reverso por timeout del emisor (asis)

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

- **Spike:** SPIKE-001
- **Generated:** 2026-10-24 by run-dry-run-001.py
- **Sources processed:** ASIS-REV-proceso-reverso

## Summary
El As-Is nuevo baja el timeout a 30 segundos, exige emisores autorizados y agrega una cola manual. El timeout está redactado como intención («se debe»), por eso esa unidad queda en confianza M.

## Knowledge Units

### KU-ASIS-REV-001
- **step:** 1. Validar al emisor
- **type:** authorization
- **statement:** Cuando el emisor no está en la lista de emisores autorizados, el sistema rechaza la transacción antes de enviarla.
- **source:** doc:ASIS-REV-proceso-reverso.md#1.1
- **excerpt:**
  > Si no está, la transacción se rechaza antes de salir.
- **confidence:** H
- **status:** proposed
- **glossary_terms:** emisor, autorizacion
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-ASIS-REV-002
- **step:** 2. Enviar el reverso
- **type:** routing
- **statement:** Cuando se dispara un reverso, el sistema lo envía al adquirente.
- **source:** doc:ASIS-REV-proceso-reverso.md#2.1
- **excerpt:**
  > Cuando se dispara un reverso, el switch lo envía al adquirente.
- **confidence:** H
- **status:** proposed
- **glossary_terms:** reverso, adquirente
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-ASIS-REV-003
- **step:** 3. Esperar respuesta del emisor
- **type:** timing/SLA
- **statement:** Cuando el emisor no responde en 30 segundos, el sistema genera un reverso automático hacia el adquirente.
- **source:** doc:ASIS-REV-proceso-reverso.md#3.2
- **excerpt:**
  > Si no se recibe respuesta del emisor en 30 segundos, se debe generar el reverso automático hacia el adquirente.
- **confidence:** M
- **status:** proposed
- **glossary_terms:** reverso, emisor, adquirente, timeout
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-ASIS-REV-004
- **step:** 4. Fallo del reverso
- **type:** exception-handling
- **statement:** Cuando el reverso automático falla, el sistema deja la transacción en una cola manual.
- **source:** doc:ASIS-REV-proceso-reverso.md#4.1
- **excerpt:**
  > Si el reverso automático falla, la transacción queda en una cola manual para que operaciones la retome.
- **confidence:** M
- **status:** proposed
- **glossary_terms:** reverso, cola manual
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24
