# Read three numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Find the largest number
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

# Output the largest number
print("The largest number is:", largest)

'''# Output:
Enter first number: 5
Enter second number: 10
Enter third number: 3
The largest number is: 10.0'''