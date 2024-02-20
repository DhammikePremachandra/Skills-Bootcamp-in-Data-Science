"""
Calculate the Total Stock Worth in the cafe
"""

# Creating a list called "menu", which contains items sold in the cafe 
menu = ["Tea", "Cappuccino", "Latte", "Americano", "Mocha", "Flat White", "Hot Chocolate", "Croissant" ]

# Creating a dictionary called "stock", which contains the stock values for each item on the "menu" list
stock = {"Tea" : 100, "Cappuccino" : 80 , "Latte" : 90, "Americano": 70, "Mocha" : 60, "Flat White" : 50, "Hot Chocolate" : 40, "Croissant" : 30}

# Creating a dictionary called "price", which contains the prices for each item on the "menu" list 
price = {"Tea" : 2.00, "Cappuccino" : 2.75 , "Latte" : 2.70, "Americano": 2.40, "Mocha" : 2.90, "Flat White" : 2.80, "Hot Chocolate" : 2.95, "Croissant" : 1.75}

# Function to calculate the total stock worth of the available stock in the cafe 
def total_stock():

    # Creating a varaible called "total_stock_worth" to store total stock worth in the cafe and asigned it to 0 
    total_stock_worth = 0

    # Loop through the menu list to get stock and price dictionary keys and access its values according to
    for item in menu:

        # Creating variable called "stock_quantity" to get the stock quantity for the item   
        stock_quantity = stock.get(item, 0) #  defaulting to 0 if not found  

        # Creating variable called "items_price" to get the price for the item
        items_price = price.get(item, 0) # defaulting to 0 if not found 

        # Calculating the total stock worth the current item and add it to the total_stock_worth
        total_stock_worth += stock_quantity * items_price
    
    # Returning the results
    return total_stock_worth
    

# Calling  the function "total_stock" to calculate the total stock worth
total_stock_worth_in_cafe = total_stock()

# Output the results using f-strings 
print(f"Total stock worth in the cafe: {total_stock_worth_in_cafe} pounds")  