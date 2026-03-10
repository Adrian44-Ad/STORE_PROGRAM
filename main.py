#STORE_MAIN_PROGRAM

from registration import Registration
from info_list    import List
from revenue      import Revenue

# THE PRESENTATION OF SYSTEM
print ('''\n                 WELCOME TO THE STORE MANAGEMENT               ''')
print ("=" * 60)

# INCLUDES THE REGISTRATION FUNCTION ASSINGNED TO Register VARIABLE
Register = Registration()

# THEN INCLUDES THE LIST FUNCTION TO LIST TOTAL LOGS
List(Register)

# FINALLY INCLUDES THE REVENUE FUNCTION ASSINGNED TO A VARIABLE
# THE FUNCTION MULTIPLY THE PRICES AND PRODUCTS QUANTITY AND ADD ALL RESULTS
total_revenue = Revenue(Register)

print(f"Total Revenue: ${total_revenue}\n")

