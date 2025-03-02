import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (CORS)

@app.route("/", methods=["GET"])
def home():
    return "Webhook server running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensaje recibido:", data)
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Usa la variable de entorno PORT
    app.run(host="0.0.0.0", port=port)
