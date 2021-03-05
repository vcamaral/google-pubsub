import base64

from flask import Flask, request

app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
    req = request.json
    print(f"Request: {req}")

    data = base64.b64decode(req["message"]["data"]).decode("utf-8")
    print(f"Decoded data: {data}")

    return "", 200


app.run()
