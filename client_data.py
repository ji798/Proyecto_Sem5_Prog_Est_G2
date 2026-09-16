def get_client_data():
    try: 
        first_name = input("Ingrese el nombre del cliente: ")
        last_name = input("Ingrese el apellido del cliente: ")
        client_type = input("Ingrese el tipo de cliente (Regular, Premium, VIP): ")
        
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
        return None

    client_data = {
        "nombre": first_name,
        "apellido": last_name,
        "tipo_cliente": client_type,
        
    }

    return client_data