from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

# Variables globales
ci = ""
codRes = ""
menRes = ""
accion = ""

@cliente.route('/cliente', methods=['POST'])
def llamarServicioCliente():
    global ci
    ci = request.json['ci']
    inicializarVariables(ci)
    
    salida = { 'codRes': codRes, 'menRes': menRes, 'ci': ci, 'accion': accion }
    return jsonify(salida)

def inicializarVariables(ci):
    global codRes, menRes, accion
    
    # clientes registrados
    clientes_registrados = [
        "4133266",
        "1234567", 
        "9876543",
        "5555555",
        "1111111"
    ]
    
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    try:
        print(f"Verificar cliente con CI: {ci}")
        
        if str(ci) in clientes_registrados:
            print("Cliente encontrado en el sistema")
            accion = "Success"
        else:
            print("Cliente no encontrado en el sistema")
            accion = "Cliente no está en el sistema"
            codRes = 'ERROR'
            menRes = 'Error cliente'
            
    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"
    
    return codRes, menRes, accion
