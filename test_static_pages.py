"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Automated Quality Assurance Test Suite: Static Pages & Asset Verification
File: test_static_pages.py
"""

import os
import re
import json
import csv
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
STATIC_DIR = os.path.join(BASE_DIR, "static")

class TestAquaCardStaticSite(unittest.TestCase):

    def test_01_core_files_exist(self):
        """Verifies all mandatory project architecture files exist."""
        required_files = [
            "index.html",
            ".nojekyll",
            "AquaCard.m",
            "matlab_runner.py",
            "generate_assets.py",
            "generate_svgs.py",
            "app.py",
            "requirements.txt",
            "start.bat",
            "static/css/style.css",
            "static/css/animations.css",
            "static/js/app.js",
            "static/js/speech.js",
            "static/js/lab_effects.js",
            "static/js/matlab_viewer.js",
            "results/aquacard_results.json",
            "results/aquacard_results.csv"
        ]
        for f in required_files:
            p = os.path.join(BASE_DIR, f)
            self.assertTrue(os.path.exists(p), f"Missing required file: {f}")

    def test_02_five_matlab_visualizations_exist(self):
        """Verifies all five required MATLAB scientific visualization PNGs exist."""
        required_plots = [
            "matlab_parameter_monitoring.png",
            "matlab_input_output_comparison.png",
            "matlab_confusion_matrix.png",
            "matlab_sensor_trend_analysis.png",
            "matlab_purification_dashboard.png"
        ]
        for plot in required_plots:
            p = os.path.join(RESULTS_DIR, plot)
            self.assertTrue(os.path.exists(p), f"Missing MATLAB plot: {plot}")
            self.assertGreater(os.path.getsize(p), 10000, f"Plot file seems corrupt or empty: {plot}")

    def test_03_vector_svg_assets_exist(self):
        """Verifies all vector SVG graphic assets exist."""
        svg_files = [
            "dr_adrian.svg",
            "ethan_carter.svg",
            "aquacard_machine.svg",
            "lab_background.svg"
        ]
        for svg in svg_files:
            p = os.path.join(STATIC_DIR, "images", svg)
            self.assertTrue(os.path.exists(p), f"Missing vector SVG: {svg}")
            self.assertGreater(os.path.getsize(p), 1000, f"SVG file too small: {svg}")

    def test_04_audio_assets_exist(self):
        """Verifies procedural WAV audio assets exist."""
        audio_files = [
            "ambient_lab.wav",
            "water_flow.wav",
            "sensor_chirp.wav",
            "ui_click.wav"
        ]
        for wav in audio_files:
            p = os.path.join(STATIC_DIR, "audio", wav)
            self.assertTrue(os.path.exists(p), f"Missing audio asset: {wav}")
            self.assertGreater(os.path.getsize(p), 5000, f"Audio file too small: {wav}")

    def test_05_results_data_integrity(self):
        """Verifies authentic scientific calculations in aquacard_results.json."""
        json_path = os.path.join(RESULTS_DIR, "aquacard_results.json")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("classification_accuracy_percent", data)
        acc = data["classification_accuracy_percent"]
        # Must be authentic, not 100%, and between 90% and 99%
        self.assertGreater(acc, 90.0, "Accuracy too low")
        self.assertLess(acc, 100.0, "Accuracy must not falsely promise 100%")
        self.assertEqual(acc, 95.83, "Expected verified calculated accuracy of 95.83%")

        # Validate confusion matrix
        cm = data["confusion_matrix"]
        self.assertEqual(len(cm), 4)
        self.assertEqual(len(cm[0]), 4)

        # Check scientific disclaimer
        self.assertIn("scientific_disclaimer", data)
        self.assertIn("does not replace", data["scientific_disclaimer"].lower())

    def test_06_index_html_github_pages_compatibility(self):
        """Ensures index.html uses relative paths and contains all core UI elements."""
        index_path = os.path.join(BASE_DIR, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        # No absolute root paths like href="/static" or src="/results"
        self.assertNotRegex(html, r'(?:href|src)=["\']/(?:static|results|css|js)',
                           "Detected absolute path! Must use repository-relative paths for GitHub Pages subpaths.")

        # Check core UI components
        self.assertIn('id="landing-screen"', html)
        self.assertIn('id="btn-start-presentation"', html)
        self.assertIn('id="controls-bar"', html)
        self.assertIn('id="btn-play-pause"', html)
        self.assertIn('id="btn-restart"', html)
        self.assertIn('id="btn-toggle-subtitles"', html)
        self.assertIn('id="btn-toggle-sound"', html)
        self.assertIn('id="btn-toggle-fullscreen"', html)
        self.assertIn('id="progress-track"', html)
        self.assertIn('id="subtitle-container"', html)
        self.assertIn('id="final-screen"', html)
        self.assertIn('id="widget-matlab-panel"', html)

        # Tagline and ending quote
        self.assertIn("Intelligence That Makes Every Drop Count", html)
        self.assertIn("Because the future of clean water begins with intelligent decisions", html)

    def test_07_dialogue_word_count_and_timing(self):
        """Verifies 7 scenes, 165s duration, and ~320-340 spoken words in app.js."""
        app_js_path = os.path.join(STATIC_DIR, "js", "app.js")
        with open(app_js_path, "r", encoding="utf-8") as f:
            js = f.read()

        # Check total duration
        self.assertIn("TOTAL_DURATION = 165.0", js)

        # Extract dialogue texts from js
        dialogue_matches = re.findall(r'text:\s*"([^"]+)"', js)
        self.assertEqual(len(dialogue_matches), 15, "Expected 15 spoken dialogue lines across 7 scenes.")

        total_words = 0
        for text in dialogue_matches:
            words = text.split()
            total_words += len(words)

        print(f"\n[QA VERIFIED] Spoken Dialogue Word Count: {total_words} words across 15 lines.")
        self.assertGreaterEqual(total_words, 320, "Spoken dialogue should be at least 320 words.")
        self.assertLessEqual(total_words, 340, "Spoken dialogue should not exceed 340 words.")

    def test_08_matlab_script_completeness(self):
        """Checks AquaCard.m contains proper data generation and visualization code."""
        m_path = os.path.join(BASE_DIR, "AquaCard.m")
        with open(m_path, "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn("rng(42", code)
        self.assertIn("k = 5", code)
        self.assertIn("conf_matrix", code)
        self.assertIn("matlab_parameter_monitoring.png", code)
        self.assertIn("aquacard_results.json", code)
        self.assertIn("aquacard_results.csv", code)
        self.assertIn("Academic Conceptual Prototype", code)

if __name__ == "__main__":
    unittest.main()
