@echo off
SETLOCAL EnableDelayedExpansion
D:
SET CurrentDir="%~dp0"

ECHO The current file path this bat file is executing in is the following:

ECHO %CurrentDir%

REM Change to the directory where the batch file is located
cd /d %CurrentDir%

REM Get the list of available Python versions
for /f "delims=" %%i in ('pyenv versions') do (
    set "versions=!versions!%%i
"
)

echo Available Python versions:
echo -------------------------
echo !versions!

REM Prompt the user to enter the desired Python version
set /p version="Enter the desired Python version: "

REM Create the virtual environment with the selected version
pyenv local %version% && python -m venv .venv && .venv\Scripts\activate && python -m pip install --upgrade pip && pip install -r requirements.txt
echo Virtual environment created with Python %version%.

pause
