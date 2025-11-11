@echo off
chcp 65001 > nul
echo Starting Midnight Friends Customer Service API Server...
echo.

:start
python customer_service_api.py
echo.
echo Server stopped unexpectedly, restarting in 5 seconds...
timeout /t 5 /nobreak > nul
echo.
goto start