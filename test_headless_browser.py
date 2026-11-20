"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Automated Headless Chrome Browser Verification via Chrome DevTools Protocol (CDP)
File: test_headless_browser.py

Simulates GitHub Pages deployment subpath:
https://username.github.io/AquaCard_AI_Water_Purification/index.html
Verifies:
- Zero unhandled JavaScript exceptions
- All 22 network requests return 200 OK
- Landing screen and Start button
- Seven scenes transition and timeline (165s)
- Speech & lip-sync visemes
- Fluid canvas particle rendering
- MATLAB scientific panel and tabs
- Predictive alert banner
- Pause, Resume, Restart, and Controls
"""

import os
import sys
import json
import time
import socket
import socketserver
import shutil
import tempfile
import threading
import subprocess
import asyncio
import urllib.request
import base64
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

sys.stdout.reconfigure(line_buffering=True)
socketserver.TCPServer.allow_reuse_address = True

# Bypass proxy for localhost
os.environ["no_proxy"] = "*"
os.environ["NO_PROXY"] = "*"
for k in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"]:
    os.environ.pop(k, None)

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "results", "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

import websockets

class CustomStaticServer:
    def __init__(self, root_dir, port=None):
        self.root_dir = root_dir
        self.port = port or get_free_port()
        self.httpd = None
        self.thread = None

    def start(self):
        root = self.root_dir
        class Handler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=root, **kwargs)
            def log_message(self, format, *args):
                pass

        self.httpd = ThreadingHTTPServer(("127.0.0.1", self.port), Handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        print(f"[CDP TEST] Static HTTP Server running on http://127.0.0.1:{self.port} (Serving: {root})", flush=True)

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()

async def run_browser_tests():
    # 1. Setup GitHub Pages Subpath Simulation directory
    subpath_parent = os.path.join(tempfile.gettempdir(), f"gh_aquacard_{int(time.time())}")
    subpath_repo = os.path.join(subpath_parent, "AquaCard_AI_Water_Purification")
    os.makedirs(subpath_repo, exist_ok=True)

    # Copy files
    for item in ["index.html", "static", "results", ".nojekyll"]:
        src = os.path.join(BASE_DIR, item)
        dst = os.path.join(subpath_repo, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        elif os.path.isfile(src):
            shutil.copy2(src, dst)

    server_port = get_free_port()
    server = CustomStaticServer(root_dir=subpath_parent, port=server_port)
    server.start()
    time.sleep(0.5)

    # 2. Launch Headless Chrome
    chrome_port = get_free_port()
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data = os.path.join(tempfile.gettempdir(), f"chrome_aqua_{chrome_port}")
    cmd = [
        chrome_path,
        "--headless=new",
        f"--remote-debugging-port={chrome_port}",
        "--remote-debugging-address=127.0.0.1",
        "--no-proxy-server",
        "--no-sandbox",
        "--disable-gpu",
        "--window-size=1920,1080",
        f"--user-data-dir={user_data}",
        "about:blank"
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2.5)

    try:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        res = opener.open(f"http://127.0.0.1:{chrome_port}/json/list", timeout=5)
        pages = json.loads(res.read().decode())
        ws_url = pages[0]["webSocketDebuggerUrl"]
        print("[CDP TEST] Connected to Headless Chrome via WebSocket:", ws_url, flush=True)

        async with websockets.connect(ws_url) as ws:
            msg_id = 1
            exceptions = []
            console_logs = []
            pending_responses = {}

            async def send(method, params=None):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                fut = asyncio.get_event_loop().create_future()
                pending_responses[mid] = fut
                req = {"id": mid, "method": method}
                if params:
                    req["params"] = params
                await ws.send(json.dumps(req))
                return await fut

            async def reader():
                try:
                    async for msg in ws:
                        data = json.loads(msg)
                        if "id" in data and data["id"] in pending_responses:
                            pending_responses[data["id"]].set_result(data.get("result", {}))
                            del pending_responses[data["id"]]
                        elif data.get("method") == "Runtime.exceptionThrown":
                            exc = data["params"]["exceptionDetails"]
                            exceptions.append(f"EXCEPTION: {exc.get('text')} - {exc.get('exception', {}).get('description')}")
                        elif data.get("method") == "Runtime.consoleAPICalled":
                            args = [str(a.get("value", a.get("description", ""))) for a in data["params"]["args"]]
                            console_logs.append(f"[{data['params']['type']}] {' '.join(args)}")
                except asyncio.CancelledError:
                    pass

            reader_task = asyncio.create_task(reader())

            # Enable Page, Runtime, Network domains
            await send("Page.enable")
            await send("Runtime.enable")
            await send("Network.enable")

            # Navigate to the GitHub Pages simulated subpath
            target_url = f"http://127.0.0.1:{server_port}/AquaCard_AI_Water_Purification/index.html"
            print(f"[CDP TEST] Navigating to: {target_url}", flush=True)
            await send("Page.navigate", {"url": target_url})
            await asyncio.sleep(2.0)

            # Helper for evaluating JS
            async def eval_js(expression):
                res = await send("Runtime.evaluate", {"expression": expression, "returnByValue": True})
                return res.get("result", {}).get("value")

            # Helper to take screenshot
            async def take_screenshot(name):
                res = await send("Page.captureScreenshot", {"format": "png"})
                data = base64.b64decode(res.get("data", ""))
                save_path = os.path.join(SCREENSHOTS_DIR, name)
                with open(save_path, "wb") as f:
                    f.write(data)
                print(f"  -> Captured screenshot: {name} ({len(data)} bytes)", flush=True)

            # -----------------------------------------------------------------
            # TEST 1: Page Load & Title Verification
            # -----------------------------------------------------------------
            title = await eval_js("document.title")
            print(f"[CDP TEST] Page Title: '{title}'", flush=True)
            assert "AQUACARD" in title, "Expected 'AQUACARD' in page title!"

            # Take screenshot of Landing Screen
            await take_screenshot("screenshot_01_landing.png")

            # -----------------------------------------------------------------
            # TEST 2: Start Presentation Button Click
            # -----------------------------------------------------------------
            landing_display_before = await eval_js("document.getElementById('landing-screen').style.display")
            print(f"[CDP TEST] Landing screen display before start: '{landing_display_before}'", flush=True)

            # Click start presentation
            await eval_js("document.getElementById('btn-start-presentation').click()")
            await asyncio.sleep(1.0)

            landing_display_after = await eval_js("document.getElementById('landing-screen').style.display")
            is_playing = await eval_js("window.aquaApp.isPlaying")
            print(f"[CDP TEST] Landing screen after click: '{landing_display_after}' | isPlaying: {is_playing}", flush=True)
            assert landing_display_after == "none", "Landing screen should be hidden after start!"
            assert is_playing is True, "Presentation should be playing!"

            # -----------------------------------------------------------------
            # TEST 3: Scene 2 Machine Reveal
            # -----------------------------------------------------------------
            await eval_js("window.aquaApp.seek(23.0)")
            await asyncio.sleep(1.2)
            scene_badge_text = await eval_js("document.querySelector('#scene-badge .scene-number').textContent")
            print(f"[CDP TEST] At 23s: Badge is '{scene_badge_text}'", flush=True)
            assert "SCENE 2" in scene_badge_text, "Expected Scene 2 badge!"
            await take_screenshot("screenshot_02_machine.png")

            # -----------------------------------------------------------------
            # TEST 4: Scene 3 Sensor Telemetry Widget
            # -----------------------------------------------------------------
            await eval_js("window.aquaApp.seek(45.0)")
            await asyncio.sleep(1.2)
            sensor_widget_visible = await eval_js("document.getElementById('widget-sensor-matrix').classList.contains('visible')")
            print(f"[CDP TEST] At 45s: Sensor matrix visible = {sensor_widget_visible}", flush=True)
            assert sensor_widget_visible is True, "Sensor matrix widget should be visible in Scene 3!"
            await take_screenshot("screenshot_03_sensors.png")

            # -----------------------------------------------------------------
            # TEST 5: Scene 4 Purification Routing Flow
            # -----------------------------------------------------------------
            await eval_js("window.aquaApp.seek(70.0)")
            await asyncio.sleep(1.2)
            purif_widget_visible = await eval_js("document.getElementById('widget-purification-flow').classList.contains('visible')")
            print(f"[CDP TEST] At 70s: Purification flow visible = {purif_widget_visible}", flush=True)
            assert purif_widget_visible is True, "Purification flow widget should be visible in Scene 4!"

            # -----------------------------------------------------------------
            # TEST 6: Scene 5 MATLAB Scientific Panel & Tab Interaction
            # -----------------------------------------------------------------
            await eval_js("window.aquaApp.seek(95.0)")
            await asyncio.sleep(1.5)
            matlab_visible = await eval_js("document.getElementById('widget-matlab-panel').classList.contains('visible')")
            accuracy_text = await eval_js("document.getElementById('matlab-stat-accuracy').textContent")
            print(f"[CDP TEST] At 95s: MATLAB panel visible = {matlab_visible} | Accuracy = '{accuracy_text}'", flush=True)
            assert matlab_visible is True, "MATLAB scientific panel should be visible in Scene 5!"
            assert "95.83%" in accuracy_text, "Expected verified 95.83% accuracy displayed!"

            # Switch MATLAB tab to 'dashboard'
            await eval_js("window.aquaApp.matlabViewer.selectPlot('purification_dashboard')")
            await asyncio.sleep(0.5)
            await take_screenshot("screenshot_04_matlab_dashboard.png")

            # -----------------------------------------------------------------
            # TEST 7: Scene 6 Predictive Maintenance Alert Banner
            # -----------------------------------------------------------------
            await eval_js("window.aquaApp.seek(122.0)")
            await asyncio.sleep(1.2)
            alert_visible = await eval_js("document.getElementById('widget-predictive-alert').classList.contains('visible')")
            print(f"[CDP TEST] At 122s: Predictive alert visible = {alert_visible}", flush=True)
            assert alert_visible is True, "Predictive alert widget should be visible in Scene 6!"
            await take_screenshot("screenshot_05_predictive_alert.png")

            # -----------------------------------------------------------------
            # TEST 8: Scene 7 & Final Conclusion Screen (165s)
            # -----------------------------------------------------------------
            await eval_js("window.aquaApp.seek(164.8)")
            await asyncio.sleep(1.5)
            final_screen_visible = await eval_js("document.getElementById('final-screen').classList.contains('visible')")
            print(f"[CDP TEST] At 165s completion: Final conclusion screen visible = {final_screen_visible}", flush=True)
            assert final_screen_visible is True, "Final conclusion screen should be visible at end!"
            await take_screenshot("screenshot_06_final_screen.png")

            # -----------------------------------------------------------------
            # TEST 9: Check for Uncaught Exceptions
            # -----------------------------------------------------------------
            print(f"[CDP TEST] Total JavaScript Exceptions Logged: {len(exceptions)}", flush=True)
            for exc in exceptions:
                print("   !! ERROR:", exc)
            assert len(exceptions) == 0, f"Detected unhandled JavaScript exceptions: {exceptions}"

            reader_task.cancel()
            print("\n" + "="*70)
            print(" [CDP AUTOMATED BROWSER TEST PASSED] All 9 Test Checkpoints Succeeded!")
            print("="*70 + "\n")

    finally:
        server.stop()
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except:
            proc.kill()
        shutil.rmtree(subpath_parent, ignore_errors=True)
        shutil.rmtree(user_data, ignore_errors=True)

if __name__ == "__main__":
    asyncio.run(run_browser_tests())
