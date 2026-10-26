"""Servicio HTTP del PoC. Contenedor 1."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from reverso_core import decidir, parse_issuer_timeouts

DEFAULT_TIMEOUT_S = int(os.environ.get("DEFAULT_TIMEOUT_S", "25"))
ISSUER_MAP = parse_issuer_timeouts(os.environ.get("ISSUER_TIMEOUTS", "A=20"))
CORS_ORIGIN = os.environ.get("CORS_ORIGIN", "*")


class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if self.path != "/health":
            self._send(404, {"error": "no existe"})
            return
        self._send(200, {"status": "ok"})

    def do_POST(self):
        if self.path != "/v1/autorizaciones":
            self._send(404, {"error": "no existe"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            result = decidir(
                body["emisor_id"],
                bool(body["respondio"]),
                int(body["transcurrido_s"]),
                DEFAULT_TIMEOUT_S,
                ISSUER_MAP,
            )
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            self._send(400, {"error": "cuerpo inválido"})
            return
        print(
            f"level=INFO msg=decision emisor={result['emisor_id']} reverso={result['reverso']}",
            flush=True,
        )
        self._send(200, result)

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", CORS_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Max-Age", "600")

    def _send(self, status, payload):
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self._cors_headers()
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, fmt, *args):
        return


def make_server(port=8080):
    return ThreadingHTTPServer(("0.0.0.0", port), Handler)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"level=INFO msg=escuchando port={port}", flush=True)
    make_server(port).serve_forever()
