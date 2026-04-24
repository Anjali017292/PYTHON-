cost_price=float(input("Enter cost price"))
if(cost_price<=0):
    print("Invalid cost price")
    exit()
else:
    selling_price=float(input("Enter selling price"))
    if(selling_price<=0):
        print("Invalid selling price")
        exit()
    else:
        if(selling_price>cost_price):
            print("Profit:",selling_price-cost_price)
        elif cost_price>selling_price:
            print("Loss:",cost_price-selling_price)
        else:
            print("No profit No loss")