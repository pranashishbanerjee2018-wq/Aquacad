"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Academic Conceptual Prototype & Simulation Platform
File: app.py

Flask Development Server for Local Testing & Dynamic MATLAB Execution.
Supports both static deployment and dynamic API querying.
"""

import os
import json
from flask import Flask, render_template, jsonify, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

@app.route("/")
def index():
    """Serves the master presentation interface."""
    return render_template("index.html")

@app.route("/results/<path:filename>")
def serve_results(filename):
    """Serves results artifacts (PNGs, JSON, CSV)."""
    return send_from_directory(RESULTS_DIR, filename)

@app.route("/api/results", methods=["GET"])
def get_results():
    """Returns the precomputed authentic scientific results."""
    json_path = os.path.join(RESULTS_DIR, "aquacard_results.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "Results not yet computed"}), 404

@app.route("/api/run-matlab", methods=["POST", "GET"])
def trigger_matlab():
    """Executes matlab_runner.py dynamically and returns the latest metrics."""
    try:
        import matlab_runner
        res = matlab_runner.run_simulation()
        return jsonify(res)
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == "__main__":
    print("\n" + "="*70)
    print(" AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION")
    print(" Local Flask Development Server Starting...")
    print(" Access presentation locally at: http://127.0.0.1:5000")
    print("="*70 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=False)
