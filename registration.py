# REGISTER MODULE

def registration ():

    print ("Enter the Product name, the Price and quantity of product units")
    print ("------------------------------------------------------------------")

    product = input("Product name?: ")
    price   = int(input("The Product Price?: "))
    quantity = int(input("Quantity of Products?: "))


    sales = input("Do you want to register more sales? (Y/N): ")[0].lower()


    while sales == 'y':


        products_log = {
            "products" : [product],
            "prices"   : [price],
            "quantity" : [quantity]
        }


        sales_list = []
        prices_list = []

        sales_list.append(products_log)
        prices_list.append(products_log["prices"])

        sales = input("Do you want to register more sales again? (Y/N): ")[0].lower()

        
    
registration()


