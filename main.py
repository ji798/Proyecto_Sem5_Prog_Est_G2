import calculate
import client_data
import shipping_fee


def menu():
    print("=== Menú de opciones ===")
    print("1. Ingresar datos del cliente")
    print("2. realizar cotización")
    print("3. Salir")

def main():
    # Aquí puedes llamar a las funciones que necesites para ejecutar tu programa
    while True: 
        menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            client_data = client_data.get_client_data()

            if client_data is not None:
                print("Datos del cliente:")
                print(f"Nombre: {client_data['nombre']}")
                print(f"Apellido: {client_data['apellido']}")
                print(f"Tipo de cliente: {client_data['tipo_cliente']}")
                print(f"Zona: {client_data['zona']}")