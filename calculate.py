def cal_subtotal(amount = 1, price = 0.0):
    
    return amount * price

def cal_discount(subtotal = 0.0, percentage = 0.0):
    
    return subtotal * (percentage / 100)

def cal_total(subtotal = 0.0, discount = 0.0):
    
    return subtotal - discount

