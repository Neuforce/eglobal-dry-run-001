### KU-CODE-EX-011
- **step:** 3. Esperar respuesta del emisor
- **type:** timing/SLA
- **statement:** Cuando el emisor no responde en **25 segundos** (valor por defecto, configurable por `issuer.timeout.ms`), el switch genera un reverso automático.
- **source:** code:example-org/switch-core/src/main/java/ex/ReversalScheduler.java:42-44@a1b2c3d
- **excerpt:**
  > `@Value("${issuer.timeout.ms:25000}") private long issuerTimeoutMs;`
- **confidence:** M  _(runtime config may override the default)_
- **status:** approved
- **reviewer:** Tech Lead (ejemplo), 2026-10-11
