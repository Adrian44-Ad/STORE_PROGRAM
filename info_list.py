# LIST SALES INFORMATION

def List(product_list):
    
    print("\n - Today's Sales Summary - \n")
    
    for i, products in enumerate(product_list, start= 0):
        
        print (f'''
            Product ID # {i + 1}
                Product:   {products["product"]}
                Price:    ${products["price"]}
                Quantity:  {products["quantity"]}
            --------------------------------------
            ''')