# Domain Glossary (business ↔ code)

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

| Business term (ES) | Definition | Synonyms / acronyms | Code identifiers (classes, tables, fields) | Status |
|---|---|---|---|---|
| emisor | Institución que autoriza la transacción | issuer | EMISORES_AUTORIZADOS, ISSUER_TIMEOUT_S | proposed |
| adquirente | Destino del reverso | acquirer | DESTINO_REVERSO | proposed |
| reverso | Devolución automática de la transacción | reversal | dispara_reverso | proposed |
| timeout | Segundos de espera al emisor | tiempo de espera | ISSUER_TIMEOUT_S | proposed |
| cola manual | Bandeja de operaciones si el reverso falla | cola | — | proposed |
