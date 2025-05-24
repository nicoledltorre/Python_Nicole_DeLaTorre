from flask import Flask, request, jsonify
from cliente import verificar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():
    data = request.get_json()
    if not data or 'ci' not in data:
        return jsonify({
            "accion": "No se ha enviado la cédula",
            "codRes": "ERROR",
            "menRes": "Debe enviar la cédula (ci)",
            "ci": None
        }), 400

    ci = data['ci']
    resultado = verificar_cliente(ci)
    return jsonify(resultado)

if __name__ == '_main_':
    app.run(host='localhost', debug = True, port = 5003)