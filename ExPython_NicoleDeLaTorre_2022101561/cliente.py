from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def llamaserv():
    data = request.get_json()
    ci = data.get('ci') if data else None
    
    if not ci:
        return jsonify({
            'codRes': 'ERROR',
            'menRes': 'No se encuentra el campo ci',
            'ci': '',
            'accion': 'Datos incorrectos'
        }), 400

    codRes, menRes, accion = proceso(ci)
    
    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion
    }
    return jsonify(salida)

def proceso(ci):
    ciLocal = "4133266"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    try:
        if ciLocal == ci:
            accion = "Success"
        else:
            print("Cliente no existe")
            accion = "el Cliente no figura en el sistema"
            codRes = 'ERROR'
            menRes = 'Error el cliente no fue encontrado'
            
    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error en el sistema"

    return codRes, menRes, accion