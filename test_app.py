"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Automated Quality Assurance: Flask Application Test Suite
File: test_app.py
"""

import os
import unittest
import json
from app import app

class TestAquaCardFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_01_index_route(self):
        """Verifies root route serves presentation HTML successfully."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AQUACARD", response.data)
        self.assertIn(b"Intelligence That Makes Every Drop Count", response.data)

    def test_02_results_artifacts_route(self):
        """Verifies serving results artifacts (JSON and PNGs)."""
        response = self.client.get("/results/aquacard_results.json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("classification_accuracy_percent", data)
        self.assertEqual(data["classification_accuracy_percent"], 95.83)

        # Check a PNG
        response_png = self.client.get("/results/matlab_confusion_matrix.png")
        self.assertEqual(response_png.status_code, 200)
        self.assertEqual(response_png.content_type, "image/png")

    def test_03_api_results(self):
        """Verifies /api/results JSON endpoint."""
        response = self.client.get("/api/results")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["model_type"], "Supervised k-Nearest Neighbors (k=5, Standardized Euclidean)")

    def test_04_api_run_matlab(self):
        """Verifies /api/run-matlab triggering simulation engine."""
        response = self.client.post("/api/run-matlab")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("status", data)
        self.assertIn("accuracy", data)
        self.assertEqual(data["accuracy"], 95.83)

if __name__ == "__main__":
    unittest.main()
