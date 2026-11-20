"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Automated Quality Assurance: Animation & Viseme Logic Test Suite
File: test_animation_logic.py
"""

import os
import re
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class TestAquaCardAnimationLogic(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
            self.index_html = f.read()
        with open(os.path.join(BASE_DIR, "static", "js", "speech.js"), "r", encoding="utf-8") as f:
            self.speech_js = f.read()
        with open(os.path.join(BASE_DIR, "static", "js", "lab_effects.js"), "r", encoding="utf-8") as f:
            self.effects_js = f.read()
        with open(os.path.join(BASE_DIR, "static", "js", "app.js"), "r", encoding="utf-8") as f:
            self.app_js = f.read()

    def test_01_five_distinct_mouth_shapes_exist(self):
        """Verifies 5 distinct mouth shapes exist in SVG for both Adrian and Ethan."""
        mouth_visemes = [
            "adrian-mouth-rest",
            "adrian-mouth-vowel-a",
            "adrian-mouth-round-o",
            "adrian-mouth-wide-e",
            "adrian-mouth-mid",
            "ethan-mouth-rest",
            "ethan-mouth-vowel-a",
            "ethan-mouth-round-o",
            "ethan-mouth-wide-e",
            "ethan-mouth-mid"
        ]
        for v in mouth_visemes:
            self.assertIn(f'id="{v}"', self.index_html, f"Missing viseme element in SVG: {v}")

    def test_02_natural_blinking_elements_exist(self):
        """Verifies eye blink elements exist in SVG and handlers in JS."""
        self.assertIn('id="adrian-blink"', self.index_html)
        self.assertIn('id="ethan-blink"', self.index_html)
        self.assertIn('initNaturalBlinking', self.effects_js)

    def test_03_non_speaking_character_mouth_closed_logic(self):
        """Verifies speech.js enforces mouth closure on non-speaking character."""
        self.assertIn("const otherSpeaker = (speaker === 'adrian') ? 'ethan' : 'adrian';", self.speech_js)
        self.assertIn("this.setViseme(otherSpeaker, 'rest');", self.speech_js)

    def test_04_pause_resume_lip_sync_freezing(self):
        """Verifies pause() and resume() preserve and freeze lip-sync appropriately."""
        self.assertIn("pause() {", self.speech_js)
        self.assertIn("resume() {", self.speech_js)
        self.assertIn("clearInterval(this.visemeTimer)", self.speech_js)

    def test_05_seven_continuous_scenes_in_app_js(self):
        """Verifies all seven continuous scenes are mapped in app.js."""
        scenes = [
            "The Global Water Challenge",
            "Introducing AQUACARD",
            "The Sensor Intelligence",
            "AI-Powered Purification",
            "MATLAB Scientific Monitoring",
            "Intelligent Management",
            "The Future of Water Technology"
        ]
        for sc in scenes:
            self.assertIn(sc, self.app_js, f"Missing scene in app.js: {sc}")

    def test_06_machine_five_chambers_exist(self):
        """Verifies the five sequential transparent purification chambers exist in machine SVG."""
        self.assertIn('id="mach-ch1"', self.index_html)
        self.assertIn('id="mach-ch2"', self.index_html)
        self.assertIn('id="mach-ch3"', self.index_html)
        self.assertIn('id="mach-ch4"', self.index_html)
        self.assertIn('id="mach-ch5"', self.index_html)

    def test_07_fluid_particles_canvas_exists(self):
        """Verifies HTML5 canvas for fluid particles is declared and initialized."""
        self.assertIn('id="fluid-particles-canvas"', self.index_html)
        self.assertIn('initFluidCanvas', self.effects_js)

if __name__ == "__main__":
    unittest.main()
