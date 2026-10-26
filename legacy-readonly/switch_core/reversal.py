"""Switch legacy ficticio. Solo lectura. Dry-run 001. No es código de eGlobal."""

# --- rule ---
# match: emisor-autorizado
# step: 1. Validar al emisor
# type: authorization
# confidence: H
# terms: emisor, autorizacion
# statement: Cuando el emisor no está en la lista de emisores autorizados, el sistema rechaza la transacción antes de enviarla.
# excerpt: if emisor_id not in EMISORES_AUTORIZADOS:
# --- end ---
EMISORES_AUTORIZADOS = ("A", "B")


def emisor_autorizado(emisor_id):
    if emisor_id not in EMISORES_AUTORIZADOS:
        return False
    return True


# --- rule ---
# match: reverso-adquirente
# step: 2. Enviar el reverso
# type: routing
# confidence: H
# terms: reverso, adquirente
# statement: Cuando se dispara un reverso, el sistema lo envía al adquirente.
# excerpt: DESTINO_REVERSO = "adquirente"
# --- end ---
DESTINO_REVERSO = "adquirente"


# --- rule ---
# match: timeout
# step: 3. Esperar respuesta del emisor
# type: timing/SLA
# confidence: H
# terms: reverso, emisor, adquirente, timeout
# statement: Cuando el emisor no responde en 25 segundos, el sistema genera un reverso automático hacia el adquirente.
# excerpt: ISSUER_TIMEOUT_S = 25
# --- end ---
ISSUER_TIMEOUT_S = 25


# --- rule ---
# match: reintentos
# step: 3. Esperar respuesta del emisor
# type: exception-handling
# confidence: H
# terms: reverso, emisor, reintento
# statement: Cuando el emisor no responde, el sistema reintenta la consulta hasta 3 veces antes de disparar el reverso.
# excerpt: MAX_REINTENTOS = 3
# --- end ---
MAX_REINTENTOS = 3


def dispara_reverso(respondio, transcurrido_s):
    if respondio:
        return False
    return transcurrido_s >= ISSUER_TIMEOUT_S
