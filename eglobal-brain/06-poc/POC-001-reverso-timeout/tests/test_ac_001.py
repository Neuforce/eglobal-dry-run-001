"""Pruebas del slice. El nombre de cada caso cita el AC."""

import json
import os
import threading
import unittest
import urllib.request
from pathlib import Path

os.environ.setdefault("DEFAULT_TIMEOUT_S", "25")
os.environ.setdefault("ISSUER_TIMEOUTS", "A=20")

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from reverso import make_server
from reverso_core import decidir, parse_issuer_timeouts

ISSUERS = parse_issuer_timeouts("A=20")


class TestAC001(unittest.TestCase):
    def test_AC_001_1_emisor_A_a_los_20s_genera_reverso(self):
        result = decidir("A", False, 20, 25, ISSUERS)
        self.assertTrue(result["reverso"])
        self.assertEqual(result["destino"], "adquirente")
        self.assertEqual(result["timeout_s"], 20)

    def test_AC_001_2_sin_configuracion_a_los_25s_genera_reverso(self):
        result = decidir("Z", False, 25, 25, ISSUERS)
        self.assertTrue(result["reverso"])
        self.assertEqual(result["destino"], "adquirente")
        self.assertEqual(result["timeout_s"], 25)

    def test_AC_001_3_sin_configuracion_a_los_24s_no_genera_reverso(self):
        result = decidir("Z", False, 24, 25, ISSUERS)
        self.assertFalse(result["reverso"])
        self.assertIsNone(result["destino"])

    def test_AC_001_1_http(self):
        server = make_server(0)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = urllib.request.Request(
                f"http://127.0.0.1:{port}/v1/autorizaciones",
                data=json.dumps(
                    {"emisor_id": "A", "respondio": False, "transcurrido_s": 20}
                ).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(request) as response:
                body = json.loads(response.read().decode("utf-8"))
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
            self.assertTrue(body["reverso"])
            self.assertEqual(body["destino"], "adquirente")
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
