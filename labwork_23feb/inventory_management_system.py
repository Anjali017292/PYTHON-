# -------------------------------------------------------
# Function to validate stock quantity (non-negative integer)
# -------------------------------------------------------
def is_valid_stock(value):
    try:
        stock = int(value)
        if stock >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


# -------------------------------------------------------
# Inventory Management System
# -------------------------------------------------------
def inventory_management():

    data = input("Enter product stock quantities separated by space: ").split()

    stocks = []

    # Validate stock inputs
    for item in data:
        if is_valid_stock(item):
            stocks.append(int(item))
        else:
            print(f"Invalid stock ignored: {item}")

    if not stocks:
        print("No valid stock data entered.")
        return

    print("\nOriginal Stock List:", stocks)

    # Remove items with 0 stock
    filtered_stocks = []
    for stock in stocks:
        if stock > 0:
            filtered_stocks.append(stock)

    if not filtered_stocks:
        print("All items have 0 stock.")
        return

    print("After Removing 0 Stock Items:", filtered_stocks)

    # Add restock (50 units) to items below 10
    for i in range(len(filtered_stocks)):
        if filtered_stocks[i] < 10:
            original = filtered_stocks[i]
            filtered_stocks[i] += 50
            print(f"Restocked: {original} → {filtered_stocks[i]}")

    # Calculate total inventory count
    total_inventory = 0
    for stock in filtered_stocks:
        total_inventory += stock

    print("\nFinal Stock List:", filtered_stocks)
    print("Total Inventory Count:", total_inventory)


# Run Program
inventory_management()






'''output:  
Enter product stock quantities separated by space: 20 0 5 15 -3 abc
Invalid stock ignored: -3
Invalid stock ignored: abc
Original Stock List: [20, 0, 5, 15]
After Removing 0 Stock Items: [20, 5, 15]
Restocked: 5 → 55
Final Stock List: [20, 55, 15]
Total Inventory Count: 90
'''