@echo off
setlocal

set "ROOT_DIR=%~dp0.."
cd /d "%ROOT_DIR%"

if not exist .venv (
    python -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pytest tests/test_app.py
if errorlevel 1 exit /b %errorlevel%
python src/app.py
exit /b %errorlevel%
