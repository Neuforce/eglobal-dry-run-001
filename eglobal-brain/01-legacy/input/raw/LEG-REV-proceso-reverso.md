# Proceso de reverso por timeout del emisor

Documento ficticio de dry-run 001. No describe un sistema real de eGlobal.

- **Doc ID:** LEG-REV-proceso-reverso
- **Fecha del documento:** 2019-04-12
- **Proceso:** P-REV
- **Corpus:** legacy

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

Si no se recibe respuesta del emisor en 45 segundos, el switch dispara el reverso automático hacia el adquirente.

```rule
match: timeout
section: 3.2
step: 3. Esperar respuesta del emisor
type: timing/SLA
confidence: H
terms: reverso, emisor, adquirente, timeout
statement: Cuando el emisor no responde en 45 segundos, el sistema genera un reverso automático hacia el adquirente.
excerpt: Si no se recibe respuesta del emisor en 45 segundos, el switch dispara el reverso automático hacia el adquirente.
```
