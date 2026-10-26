# Knowledge: P-REV Reverso por timeout del emisor (legacy)

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

- **Spike:** SPIKE-001
- **Generated:** 2026-10-24 by run-dry-run-001.py
- **Sources processed:** LEG-REV-proceso-reverso

## Summary
El documento de 2019 dice que el reverso va al adquirente y que el timeout es de 45 segundos.

## Knowledge Units

### KU-LEG-REV-001
- **step:** 2. Enviar el reverso
- **type:** routing
- **statement:** Cuando se dispara un reverso, el sistema lo envía al adquirente.
- **source:** doc:LEG-REV-proceso-reverso.md#2.1
- **excerpt:**
  > Cuando se dispara un reverso, el switch lo envía al adquirente.
- **confidence:** H
- **status:** proposed
- **glossary_terms:** reverso, adquirente
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24

### KU-LEG-REV-002
- **step:** 3. Esperar respuesta del emisor
- **type:** timing/SLA
- **statement:** Cuando el emisor no responde en 45 segundos, el sistema genera un reverso automático hacia el adquirente.
- **source:** doc:LEG-REV-proceso-reverso.md#3.2
- **excerpt:**
  > Si no se recibe respuesta del emisor en 45 segundos, el switch dispara el reverso automático hacia el adquirente.
- **confidence:** H
- **status:** proposed
- **glossary_terms:** reverso, emisor, adquirente, timeout
- **related:**
- **reviewer:** dry-run 001 automático, 2026-10-24
