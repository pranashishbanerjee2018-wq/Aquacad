"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Full End-to-End Headless & Static Server Quality Assurance
File: test_full_presentation.py
"""

import os
import sys
import time
import socket
import threading
import http.server
import socketserver
import urllib.request
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure clean network environment
os.environ["no_proxy"] = "*"
os.environ["NO_PROXY"] = "*"
for k in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"]:
    os.environ.pop(k, None)

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

class TestAquaCardFullPresentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = get_free_port()
        root = BASE_DIR
        class CustomHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=root, **kwargs)
            def log_message(self, format, *args):
                pass

        socketserver.TCPServer.allow_reuse_address = True
        cls.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", cls.port), CustomHandler)
        cls.server_thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.server_thread.start()
        time.sleep(0.3)

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def test_01_static_server_all_assets_200_ok(self):
        """Verifies every asset referenced in presentation returns 200 OK via static server."""
        base_url = f"http://127.0.0.1:{self.port}"
        assets = [
            "/index.html",
            "/static/css/style.css",
            "/static/css/animations.css",
            "/static/js/app.js",
            "/static/js/speech.js",
            "/static/js/lab_effects.js",
            "/static/js/matlab_viewer.js",
            "/static/images/lab_background.svg",
            "/static/images/dr_adrian.svg",
            "/static/images/ethan_carter.svg",
            "/static/images/aquacard_machine.svg",
            "/results/matlab_confusion_matrix.png",
            "/results/matlab_parameter_monitoring.png",
            "/results/matlab_input_output_comparison.png",
            "/results/matlab_sensor_trend_analysis.png",
            "/results/matlab_purification_dashboard.png",
            "/results/aquacard_results.json",
            "/results/aquacard_results.csv",
            "/static/audio/ambient_lab.wav",
            "/static/audio/water_flow.wav",
            "/static/audio/sensor_chirp.wav",
            "/static/audio/ui_click.wav"
        ]

        for asset in assets:
            url = base_url + asset
            try:
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req) as resp:
                    self.assertEqual(resp.status, 200, f"Failed to fetch {asset}")
                    data = resp.read()
                    self.assertGreater(len(data), 0, f"Empty response for {asset}")
            except Exception as e:
                self.fail(f"Asset failed: {asset} -> {e}")

        print(f"[QA VERIFIED] Static HTTP Server successfully served all {len(assets)} assets with 200 OK!")

if __name__ == "__main__":
    unittest.main()
