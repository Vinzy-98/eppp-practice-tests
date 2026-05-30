@echo off
cd /d "%~dp0"
echo Starting EPPP Practice Tests server...
echo Open http://localhost:8080 in your browser
echo Press Ctrl+C to stop

where python >nul 2>nul
if %errorlevel%==0 (
    python -m http.server 8080
) else (
    where python3 >nul 2>nul
    if %errorlevel%==0 (
        python3 -m http.server 8080
    ) else (
        echo ERROR: Python is not installed or not in PATH.
        echo Download Python from https://www.python.org/downloads/
        pause
    )
)
