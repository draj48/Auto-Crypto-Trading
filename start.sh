#!/bin/bash

# Start script for Supertrend Bot
echo -e "\n🚀 Installing Python dependencies..."
pip3 install -r requirements.txt

# Start ngrok and fetch public URL
echo -e "\n🌐 Starting ngrok..."
nohup ngrok http 5000 > /dev/null &
sleep 3
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\\.ngrok-free\\.app" | head -n 1)

if [ -z "$NGROK_URL" ]; then
  echo "❌ Failed to fetch ngrok URL. Is ngrok running?"
else
  echo -e "\n🔗 Ngrok Webhook URL: $NGROK_URL/webhook"
  echo "📌 Paste this URL in your TradingView alert settings"
fi

# Start the bot
sleep 2
echo -e "\n🤖 Launching Supertrend Trading Bot...\n"
python3 trading_bot.py
