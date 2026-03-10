# PRINT TOTAL REVENUE

def Revenue (product_list):

    total = 0

    for price in product_list:

        subtotal = price ["price"] * price ["quantity"]
        total = total + subtotal


    return total