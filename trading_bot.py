import json
import time
import threading
from datetime import datetime
from flask import Flask, request, jsonify
import requests

# Load config
with open("config.json") as f:
    config = json.load(f)

API_KEY = config["delta_api_key"]
API_SECRET = config["delta_api_secret"]
USE_PERCENT = config["use_balance_percent"]
LEVERAGE = config["leverage"]
SYMBOL = config["symbol"]
BASE_URL = "https://api.delta.exchange"

app = Flask(__name__)

position_open = False
last_signal_time = None
last_signal = None

# Background thread for logging
def status_checker():
    global last_signal_time, last_signal
    while True:
        try:
            r = requests.get(BASE_URL + "/products")
            if r.status_code == 200:
                print(f"[ {datetime.now()} ] ✅ Delta Exchange connection OK")
            else:
                print(f"[ {datetime.now()} ] ❌ Delta connection FAILED (Status {r.status_code})")
        except Exception as e:
            print(f"[ {datetime.now()} ] ❌ ERROR connecting to Delta: {e}")

        if last_signal_time:
            elapsed = (datetime.now() - last_signal_time).total_seconds()
            if elapsed > 30:
                print("⚠️ No signal received from TradingView in last 30s")
            else:
                print(f"📩 Last signal: {last_signal} at {last_signal_time.strftime('%H:%M:%S')}")
        else:
            print("✅ Waiting for TradingView signal...")

        time.sleep(5)

threading.Thread(target=status_checker, daemon=True).start()

@app.route('/webhook', methods=['POST'])
def webhook():
    global position_open, last_signal_time, last_signal
    data = request.get_json()

    if not data or 'signal' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    signal = data['signal'].lower()
    last_signal_time = datetime.now()
    last_signal = signal.upper()

    if signal == 'buy' and not position_open:
        print("[ACTION] Buy signal received. Placing order...")
        position_open = True
        return jsonify({'message': 'Buy order placed'})

    elif signal == 'sell' and position_open:
        print("[ACTION] Sell signal received. Closing position...")
        position_open = False
        return jsonify({'message': 'Sell order placed'})

    return jsonify({'message': 'No action taken'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
