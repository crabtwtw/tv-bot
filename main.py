from flask import Flask, request
import requests

app = Flask(__name__)

TG_TOKEN = "你的TG_TOKEN"
CHAT_ID = "你的CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

@app.route('/')
def home():
    return "RUNNING"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    msg = f"""
📢 TradingView訊號

幣種：{data.get("symbol")}
方向：{data.get("signal")}
價格：{data.get("price")}
"""

    send(msg)

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
