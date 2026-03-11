# STORE PROGRAM MANAGEMENT

## Store Daily Sales Automation

## Project Overview

This project implements a **Python-based command line script** designed to automate the daily sales record of a small retail store.
The objective is to replace manual paper-based registration with a simple digital system that captures sales information and produces a **structured end-of-day summary**.

The system allows the store administrator to register multiple product sales during the day and automatically calculate the total revenue generated.

---

## Problem's Flow 

![Architecture Diagram] (MY_DIAGRAM_ADRIAN_PEDROZA.png)



---

## Example Output

```

                 WELCOME TO THE STORE MANAGEMENT               
============================================================
Enter the Product name, the Price and quantity of product units
--------------------------------------------------------------

Do you want to register a sale? (Y/N): y
------------------------------------------------------------
Register Sale No 1
------------------------------------------------------------
Product name: wine
The Product Price: 1200
How many products?: 3
Do you want to register sales again? (Y/N): y
------------------------------------------------------------
Register Sale No 2
------------------------------------------------------------
Product name: carrot
The Product Price: 200
How many products?: 8
Do you want to register sales again? (Y/N): y
------------------------------------------------------------
Register Sale No 3
------------------------------------------------------------
Product name: bread
The Product Price: 500
How many products?: 10
Do you want to register sales again? (Y/N): n

 - Today's Sales Summary - 


            Product ID # 1
                Product:   wine
                Price:    $1200
                Quantity:  3
            --------------------------------------
            

            Product ID # 2
                Product:   carrot
                Price:    $200
                Quantity:  8
            --------------------------------------
            

            Product ID # 3
                Product:   bread
                Price:    $500
                Quantity:  10
            --------------------------------------
            
Total Revenue: $10200

```

---

## Technologies Used

* Python 3
* VS Code

---

## Repository Structure

```
STORE_PROGRAM/
│
├── main.py
├── registration.py
├── info_list.py
├── revenue.py
└── README.md
```

