from flask import Flask, request
import requests
import os

app = Flask(__name__)

TG_TOKEN = "8728915298:AAF9WW6ddW_TTxpwEHa_hBfzaV8Qs-emy6g"
CHAT_ID = "5494623381"

def send(msg):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

@app.route('/')
def home():
    return "RUNNING"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json or {}

    msg = f"""
📢 TradingView訊號
幣種：{data.get("symbol")}
方向：{data.get("signal")}
價格：{data.get("price")}
"""

    send(msg)

    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
