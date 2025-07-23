@echo off
echo 🐪 Setting up Jmal - The Ancient Desert Wanderer...
echo.

REM Install Python dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo 🔧 Setup complete!
echo.
echo ⚠️  IMPORTANT: Make sure Ollama is running before starting Jmal!
echo    1. Install Ollama from: https://ollama.ai
echo    2. Run: ollama serve
echo    3. Install a model: ollama pull llama2
echo.
echo 🚀 Starting Jmal chatbot...
python jmal_chatbot.py

pause