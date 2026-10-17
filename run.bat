@echo off
title Ékriksie Local Server
color 0a

echo [1/3] Clearing old server tasks...
taskkill /f /im python.exe >nul 2>&1

echo [2/3] Opening browser at http://localhost:8000...
start http://localhost:8000

echo [3/3] Starting native Python server...
cd /d E:\localhost\website
python -m http.server 8000

pause