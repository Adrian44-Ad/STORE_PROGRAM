# STORE PROGRAM MANAGEMENT

## Store Daily Sales Automation

## Project Overview

This project implements a **Python-based command line script** designed to automate the daily sales record of a small retail store.
The objective is to replace manual paper-based registration with a simple digital system that captures sales information and produces a **structured end-of-day summary**.

The system allows the store administrator to register multiple product sales during the day and automatically calculate the total revenue generated.

---

## Problem Strategy

To solve the problem, the solution was designed around three fundamental ideas:

1. **Structured data storage**
2. **Separation of responsibilities using functions**
3. **Processing sales data after the registration phase**

Before starting the implementation, the workflow of the program was analyzed and represented through a **flow diagram** that describes the sequence of operations:

1. Start program
2. Request product information
3. Store the sale
4. Ask if the user wants to register another sale
5. Repeat until the user finishes
6. Process stored data
7. Display the final summary

This design ensured a clear structure before writing the code.

---

## Program Architecture

The program is organized using **modular design**, separating the logic into independent components.

### 1. Sales Registration Module

Responsible for:

* Requesting user input
* Capturing product name, price, and quantity
* Storing each sale in a list
* Allowing multiple entries until the user finishes

### 2. Product Listing Module

Responsible for:

* Iterating through stored sales
* Displaying a structured list of registered products

### 3. Revenue Calculation Module

Responsible for:

* Calculating the total revenue of the day
* Multiplying the **unit price by quantity** for each registered sale
* Accumulating the result into a final total

---

## Execution Flow

The main script coordinates the program by calling the different modules in sequence:

1. Register sales
2. Display the list of products
3. Calculate the total revenue
4. Show the final daily summary

This structure improves readability, maintainability, and code reuse.

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

