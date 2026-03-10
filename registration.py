# REGISTER MODULE

def Registration ():

    print ("Enter the Product name, the Price and quantity of product units")
    print ("--------------------------------------------------------------\n")

    counter = 1
    product_list = []
    sales = input("Do you want to register a sale? (Y/N): ")[0].lower()

    while sales == "y":
        print("-" * 60)
        print(f"Register Sale No {counter}")
        print("-" * 60)
        product = input("Product name: ")
        price   = int(input("The Product Price: "))
        quantity = int(input("How many products?: "))

        products_log = {
            "product" : product,
            "price"   : price,
            "quantity" : quantity
        }

        product_list.append(products_log)

        sales = input("Do you want to register sales again? (Y/N): ")[0].lower()

        counter = counter + 1

    return product_list


        

        



