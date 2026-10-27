# reverso-timeout Specification

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## Purpose
Decide si un emisor que no respondió ya venció su timeout y, en ese caso, arma el reverso hacia el adquirente. El valor por defecto sigue siendo 25 segundos.

## Requirements

### Requirement: Timeout de reverso configurable por emisor
The system SHALL generar un reverso hacia el adquirente cuando el emisor no responde dentro de su timeout. El valor por defecto es 25 segundos. Un emisor puede tener el suyo; en el ejemplo, el emisor A usa 20 segundos. Origen: decisión D-001 / PRD G1. Respecto del As-Is, el timeout pasa de una intención de 30 segundos a este valor configurable.

#### Scenario: Emisor A a los 20 segundos
- **WHEN** el emisor A tiene timeout de 20 s, no responde y ya van 20 s
- **THEN** se genera un reverso al adquirente

#### Scenario: Emisor sin configuración a los 25 segundos
- **WHEN** un emisor sin configuración no responde y ya van 25 s
- **THEN** se genera un reverso al adquirente

#### Scenario: Emisor sin configuración a los 24 segundos
- **WHEN** un emisor sin configuración no responde y van 24 s
- **THEN** no se genera reverso

### Requirement: Decisión sin espera de reloj
The system SHALL decidir el reverso sin esperar al reloj real en la prueba.

#### Scenario: Segundos ya transcurridos
- **WHEN** la prueba entrega los segundos ya transcurridos
- **THEN** la decisión no usa una espera real

### Requirement: Token del mock
The system SHALL exigir en el mock el token Bearer del Secret de ejemplo.

#### Scenario: Token distinto
- **WHEN** el mock recibe un token distinto del Secret de ejemplo
- **THEN** rechaza la petición
