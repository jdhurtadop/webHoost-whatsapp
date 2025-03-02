from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook server running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json  # Recibe el JSON enviado por WhatsApp
    print("Mensaje recibido:", data)  # Imprime el webhook en la consola
    return "OK", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Obtiene el puerto de Render
    app.run(host="0.0.0.0", port=port)