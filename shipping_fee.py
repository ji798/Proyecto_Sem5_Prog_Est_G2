def cal_shipping_fee(subtotal = 0.0):
    zone = input("""Ingrese la zona del cliente: 
            - distrito I
            - distrito II
            - distrito III
            - distrito IV
            - distrito V
            \n""")
    match zone:
        case "distrito I":
            shipping_fee = subtotal * 0.05
        case "distrito II":
            shipping_fee = subtotal * 0.10
        case "distrito III":
            shipping_fee = subtotal * 0.15
        case "distrito IV":
            shipping_fee = subtotal * 0.14
        case "distrito V":
            shipping_fee = subtotal * 0.07

    return shipping_fee
    
    