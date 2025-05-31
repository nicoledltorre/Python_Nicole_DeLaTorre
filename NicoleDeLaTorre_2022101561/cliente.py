def buscar_cliente(ci):
    clientes_validos = ["4133266"]
    
    if ci in clientes_validos:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }
    else:
        return {
            "accion": "El cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error el cliente no fue encontrado",
            "ci": ci
        }