# Simple Interest Calculator input and calculation
principal=float(input("Enter the principal amount: "))
if(principal<0):
    print("Principal amount cannot be negative.")
else:
    # Read the rate of interest and time from the user
    rate=float(input("Enter the rate of interest: "))
    if(rate<0):
        print("Rate of interest cannot be negative.")
    else:
        time=float(input("Enter the time in years: "))
        if(time<0):
            print("Time cannot be negative.")
        else:
            # Calculate simple interest
            simple_interest=(principal*rate*time)/100
            print("The simple interest is:", simple_interest)
            
'''# Output:
Enter the principal amount: 1000
Enter the rate of interest: 5
Enter the time in years: 2
The simple interest is: 100.0'''