# Proposal

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## Why
Los tres relatos del timeout no coinciden. El que corre es el de 25 segundos, fijo en el código. El As-Is lo redacta como una intención de 30 segundos. Este slice lo hace configurable por emisor sin perder el valor que ya corre.

## What Changes
- El timeout pasa a ser por emisor. El default es 25 segundos. El emisor A del ejemplo usa 20 segundos.
- Si el emisor no responde dentro de ese timeout, el reverso va al adquirente.
- La cola manual y los reintentos no entran en este slice.
- El emisor se simula. No hay persistencia.

## Capabilities

### New Capabilities
- `reverso-timeout`: decidir el reverso cuando el emisor no responde a tiempo.

### Modified Capabilities

## Impact
Dos contenedores (`reverso` y `emisor-mock`), contratos `POST /v1/autorizaciones` y `POST /v1/autorizar`, y `GET /health` en ambos. La imagen base de OpenShift sigue sin dato de eGlobal.
