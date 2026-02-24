# Input four numbers to find the greatest number
# Input four numbers from the user and determine which one is the greatest.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Check the greatest number
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
    # If num1 is greater than or equal to num2, num3, and num4, then num1 is the greatest number.
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
    # If num2 is greater than or equal to num1, num3, and num4, then num2 is the greatest number.
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
else:
    greatest = num4
# If num3 is greater than or equal to num1, num2, and num4, then num3 is the greatest number.
# If none of the above conditions are true, then num4 is the greatest number.
print("The greatest number is:", greatest)

'''Output:
Enter the first number: 10
Enter the second number: 20
Enter the third number: 15
Enter the fourth number: 5
The greatest number is: 20'''