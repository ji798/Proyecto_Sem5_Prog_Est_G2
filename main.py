import calculate
import client_data as client_data
import shipping_fee




def mostrar_cotizacion(product_name, amount, subtotal, discount, total, shipping_fee_value):
    print(f"Producto: {product_name}")
    print(f"cantidad: {amount}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {discount}")
    print(f"Total: {total}")
    print(f"Gastos de envío: {shipping_fee_value}")

def main():
    # Aquí puedes llamar a las funciones que necesites para ejecutar tu programa
    while True: 
        print("Seleccione una opción:")
        print("1. Realizar cotización")
        print("2. Salir")
        choice = input("Seleccione una opción: ")

        match choice:
            case "1":
                try:
                    data = client_data.get_client_data()
                    

                    if data is not None:
                        print("Datos del cliente:")
                        print(f"Nombre: {data['nombre']}")
                        print(f"Apellido: {data['apellido']}")
                        print(f"Tipo de cliente: {data['tipo_cliente']}")
                        
                
                        product_name = input("Ingrese el nombre del producto: ")
                        amount = int(input("Ingrese la cantidad de productos: "))
                        price = float(input("Ingrese el precio unitario del producto: "))

                        subtotal = calculate.cal_subtotal(amount, price)
                        discount = calculate.cal_discount(subtotal)
                        total = calculate.cal_total(subtotal, discount)
                        shipping_fee_value = shipping_fee.cal_shipping_fee(subtotal, shipping_fee.determinar_zona())

                        mostrar_cotizacion(product_name, amount, subtotal, discount, total, shipping_fee_value)

                        print("=================================================================\n")

                except ValueError:
                    print("Por favor, ingrese valores numéricos válidos.")

            case "2":
                print("Saliendo del programa...")
                print("=================================================================\n")
                break

main()