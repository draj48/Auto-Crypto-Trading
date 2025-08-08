<h1 align="center">🧠 Supertrend Auto-Trading Bot</h1>

<p align="center">
  A smart bot that connects <strong>TradingView</strong> + <strong>Delta Exchange</strong> and executes trades automatically using Supertrend signals.<br>
  No manual effort. Just plug & trade 💹
</p>

<hr>

<h2>⚙️ Features</h2>
<ul>
  <li>✅ Auto BUY on <strong>Supertrend BUY</strong> signal</li>
  <li>✅ Auto SELL when <strong>Supertrend SELL</strong> triggers</li>
  <li>🔁 Repeats forever — full cycle bot</li>
  <li>🔒 Uses only <strong>10% account balance</strong> per trade</li>
  <li>🚀 Trades with <strong>10x leverage</strong></li>
  <li>💬 Live status printed every 5 seconds</li>
  <li>🧠 Fully local setup — Ubuntu/VPS supported</li>
</ul>

<h2>📁 Folder Structure</h2>

<pre>
supertrend-bot/
├── config.json         → Your API keys and bot config
├── trading_bot.py      → Flask + bot core logic
├── requirements.txt    → Python packages
└── start.sh            → Launch ngrok + bot server
</pre>

<h2>⚡ Quick Start</h2>

<ol>
  <li><strong>Clone the repo:</strong>
    <pre>git clone https://github.com/draj48/supertrend-bot.git
cd supertrend-bot</pre>
  </li>

  <li><strong>Edit <code>config.json</code> with your API keys:</strong>
    <pre>{
  "delta_api_key": "YOUR_DELTA_API_KEY",
  "delta_api_secret": "YOUR_DELTA_API_SECRET",
  "use_balance_percent": 10,
  "leverage": 10,
  "symbol": "BTCUSDT"
}</pre>
  </li>

  <li><strong>Start the bot:</strong>
    <pre>chmod +x start.sh
./start.sh</pre>
    <p>This will also start <code>ngrok</code> and show your public webhook URL.</p>
  </li>
</ol>

<h2>📡 TradingView Webhook Setup</h2>
<ol>
  <li>Add Supertrend indicator on chart</li>
  <li>Create a new alert (on candle close)</li>
  <li>Use the ngrok URL shown by the bot as the Webhook URL</li>
  <li>In the message box, paste:
    <pre>{ "signal": "buy" }</pre>
    or
    <pre>{ "signal": "sell" }</pre>
  </li>
</ol>

<h2>📌 Notes</h2>
<ul>
  <li>⚠️ This is a demo/educational bot. Use with caution.</li>
  <li>🧪 Test in demo mode or paper trade before going live</li>
  <li>✅ Can be extended with:
    <ul>
      <li>Telegram/Slack alerts</li>
      <li>Trade logging</li>
      <li>Multiple pairs</li>
    </ul>
  </li>
</ul>

<h2>👨‍💻 Created By</h2>
<p><strong>DRAJ</strong> — A noob 💀 developer building smart bots from scratch 🔥</p>
