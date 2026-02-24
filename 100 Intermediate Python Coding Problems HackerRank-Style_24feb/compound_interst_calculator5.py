# Compound Interest Calculator input and calculation
principal = float(input("Enter the principal amount: "))

# Validate principal amount
if principal < 0:
    print("Principal amount cannot be negative.")
else:
    # Read the rate of interest and time from the user
    rate = float(input("Enter the rate of interest: "))
    
    if rate < 0:
        print("Rate of interest cannot be negative.")
    else:
        time = float(input("Enter the time in years: "))
        # Validate time
        if time < 0:
            print("Time cannot be negative.")
        else:
            # Compound Interest Formula
            amount = principal * (1 + rate / 100) ** time
            compound_interest = amount - principal
        # Output the compound interest
            print("The compound interest is:", round(compound_interest, 2))
            
'''# Output:
Enter the principal amount: 1000
Enter the rate of interest: 5
Enter the time in years: 2
The compound interest is: 102.5'''