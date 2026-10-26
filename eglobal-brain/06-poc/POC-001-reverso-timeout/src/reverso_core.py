"""Decisión de reverso. Sin red y sin reloj."""


def parse_issuer_timeouts(raw):
    found = {}
    for piece in (raw or "").split(","):
        piece = piece.strip()
        if not piece:
            continue
        emisor, seconds = piece.split("=", 1)
        found[emisor.strip()] = int(seconds)
    return found


def timeout_for(emisor_id, default_s, issuer_map):
    return issuer_map.get(emisor_id, default_s)


def decidir(emisor_id, respondio, transcurrido_s, default_s, issuer_map):
    timeout_s = timeout_for(emisor_id, default_s, issuer_map)
    reverso = (not respondio) and transcurrido_s >= timeout_s
    return {
        "emisor_id": emisor_id,
        "reverso": reverso,
        "destino": "adquirente" if reverso else None,
        "timeout_s": timeout_s,
    }
