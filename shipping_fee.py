def cal_shipping_fee(subtotal = 0.0, zone = "Nacional"):
    match zone:
        case "Nacional":
            shipping_fee = subtotal * 0.05
            return shipping_fee
        case "Centroamerica":
            shipping_fee = subtotal * 0.10
            return shipping_fee
        case "Europa":
            shipping_fee = subtotal * 0.20
            return shipping_fee
        case "Norteamerica":
            shipping_fee = subtotal * 0.18
            return shipping_fee
        case "Sudamerica":
            shipping_fee = subtotal * 0.20
            return shipping_fee

        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            

    
def determinar_zona():
    while True:
        print("Seleccione la zona de envío:")
        print("1. Nacional")
        print("2. Centroamérica")
        print("3. Europa")
        print("4. Norteamérica")
        print("5. Sudamérica")
        try:
            choice = int(input("Ingrese el número correspondiente a la zona: "))

            match choice:
                case 1:
                    return "Nacional"
                case 2:
                    return "Centroamerica"
                case 3:
                    return "Europa"
                case 4:
                    return "Norteamerica"
                case 5:
                    return "Sudamerica"
                case _:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
                
            

            
    