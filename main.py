import os
from flask import Flask
from threading import Thread
import time
import email_sender

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask activo"

@app.route('/request')
def trigger_email():
    email_sender.generar_y_enviar_reporte()
    return "Correo enviado con éxito"

def keep_alive():
    while True:
        print("Manteniendo vivo el servidor...")
        time.sleep(600)

if __name__ == '__main__':
    Thread(target=keep_alive).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
