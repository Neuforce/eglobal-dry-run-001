# Non-Functional Requirements

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

| Category | Requirement | Target / metric | Demonstrate in PoC? |
|---|---|---|---|
| Latency | Decidir el reverso sin esperar al reloj real | La prueba usa segundos ya transcurridos, no `sleep` | Y |
| Security (authN/authZ, encryption) | El mock exige el token del Secret de ejemplo | Header `Authorization: Bearer <token>` | Y |
