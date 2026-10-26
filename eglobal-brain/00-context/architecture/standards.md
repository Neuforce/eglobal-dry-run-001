# Engineering Standards

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

Valores de relleno para que el PoC de dry-run 001 pueda construirse. No son el estándar de eGlobal.

| Area | Standard |
|---|---|
| Languages and versions | Python 3.12 |
| Frameworks | Biblioteca estándar (http.server) |
| API style and spec format (REST/OpenAPI, gRPC, AsyncAPI) | HTTP JSON, sin OpenAPI en este slice |
| Naming conventions | IDs en inglés, mensajes de negocio en español |
| Error handling | Respuesta JSON con `error` y código HTTP 4xx |
| Logging format | `level=INFO msg=...` a stdout |
| Testing (frameworks, coverage expectations) | unittest, un caso por AC del slice |
| Dependency policy (approved libs, registries) | Sin dependencias de terceros |
| Code style / linters | No aplica en el dry run |
| Branching and PR rules | No aplica: esta carpeta no es un clon git |
