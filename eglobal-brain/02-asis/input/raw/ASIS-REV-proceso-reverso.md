# As-Is: reverso por timeout del emisor

Documento ficticio de dry-run 001. No describe un sistema real de eGlobal.

- **Doc ID:** ASIS-REV-proceso-reverso
- **Fecha del documento:** 2026-09-01
- **Proceso:** P-REV
- **Corpus:** as-is
- **Dueña del texto:** equipo de Alejandra (ficticio en este dry run)

## 1. Validar al emisor

### 1.1 Lista de autorizados

Solo se consulta a un emisor que esté en la lista de emisores autorizados. Si no está, la transacción se rechaza antes de salir.

```rule
match: emisor-autorizado
section: 1.1
step: 1. Validar al emisor
type: authorization
confidence: H
terms: emisor, autorizacion
statement: Cuando el emisor no está en la lista de emisores autorizados, el sistema rechaza la transacción antes de enviarla.
excerpt: Si no está, la transacción se rechaza antes de salir.
```

## 2. Enviar el reverso

### 2.1 Destino

Cuando se dispara un reverso, el switch lo envía al adquirente.

```rule
match: reverso-adquirente
section: 2.1
step: 2. Enviar el reverso
type: routing
confidence: H
terms: reverso, adquirente
statement: Cuando se dispara un reverso, el sistema lo envía al adquirente.
excerpt: Cuando se dispara un reverso, el switch lo envía al adquirente.
```

## 3. Esperar respuesta del emisor

### 3.2 Timeout

Si no se recibe respuesta del emisor en 30 segundos, se debe generar el reverso automático hacia el adquirente.

```rule
match: timeout
section: 3.2
step: 3. Esperar respuesta del emisor
type: timing/SLA
confidence: M
terms: reverso, emisor, adquirente, timeout
statement: Cuando el emisor no responde en 30 segundos, el sistema genera un reverso automático hacia el adquirente.
excerpt: Si no se recibe respuesta del emisor en 30 segundos, se debe generar el reverso automático hacia el adquirente.
```

## 4. Fallo del reverso

### 4.1 Cola manual

Si el reverso automático falla, la transacción queda en una cola manual para que operaciones la retome.

```rule
match: cola-manual
section: 4.1
step: 4. Fallo del reverso
type: exception-handling
confidence: M
terms: reverso, cola manual
statement: Cuando el reverso automático falla, el sistema deja la transacción en una cola manual.
excerpt: Si el reverso automático falla, la transacción queda en una cola manual para que operaciones la retome.
```
