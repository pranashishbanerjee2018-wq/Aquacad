@echo off
echo ==============================================================================
echo AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
echo Academic Conceptual Prototype and Simulation Engine
echo ==============================================================================
echo.
echo [1] Checking Python environment...
python -V
if %errorlevel% neq 0 (
    echo Python not found! Please install Python 3.8+ to proceed.
    pause
    exit /b
)

echo.
echo [2] Generating/Verifying Scientific Visualizations and Baseline...
python generate_assets.py

echo.
echo [3] Launching Local Presentation Server...
echo Open your browser at http://127.0.0.1:5000/
python app.py

pause
