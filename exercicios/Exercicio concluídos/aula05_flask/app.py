# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate - bash
# venv\\Scripts\\activate  - CMD
# pip install flask flask-cors

from flask import Flask, Response, request
from flask_cors import CORS
import json

app = Flask(__name__)

# Garante que o JSON será ASCII (acentos, emojis etc.)
app.config["JSON_AS_ASCII"] = False

# Configurando CORS
CORS(app)

def json_response(payload, status=200):
    #Retorna JSON com Content-Type explícito em UTF-8
    return Response(
        json.dumps(payload, ensure_ascii=False),
        status=status,
        mimetype="application/json; charset=utf-8"
    )

# "Banco de dados" em memória
users = [
    {"id": 1, "name": "Maria"},
    {"id": 2, "name": "João"},
    {"id": 3, "name": "Saulo"}
]

@app.route("/users", methods=['GET'])
def show_users():
    return json_response(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def obter_cliente(user_id):
    cliente = next((u for u in users if u['id'] == user_id), None)
    if cliente is None:
        return json_response({'error': 'Cliente não encontrado'}), 404
    return json_response(cliente), 200



if __name__ == '__main__':
    app.run(debug=True)

