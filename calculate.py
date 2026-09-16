def cal_subtotal(amount = 1, price = 0.0):
    
    return amount * price

def cal_discount(subtotal = 0.0, client_type = "regular"):
    if client_type.lower() == "regular":
        percentage = 0.05
    elif client_type.lower() == "premium":
        percentage = 0.10
    elif client_type.lower() == "vip":
        percentage = 0.15

    return subtotal * percentage

def cal_total(subtotal = 0.0, discount = 0.0, shipping_fee = 0.0):
    
    return subtotal - discount + shipping_fee

