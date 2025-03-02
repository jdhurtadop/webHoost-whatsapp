import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (CORS)

VERIFY_TOKEN = "TU_TOKEN_DE_VERIFICACION"  # Reemplázalo con el token configurado en Meta

@app.route("/", methods=["GET"])
def home():
    return "Webhook server running!"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verificación del webhook de Meta
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == VERIFY_TOKEN:
            return challenge, 200  # Responde con el challenge si el token es correcto
        return "Token inválido", 403
    
    elif request.method == "POST":
        data = request.get_json()
        print("Mensaje recibido:", data)  # Imprime la data recibida
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Usa la variable de entorno PORT
    app.run(host="0.0.0.0", port=port)
