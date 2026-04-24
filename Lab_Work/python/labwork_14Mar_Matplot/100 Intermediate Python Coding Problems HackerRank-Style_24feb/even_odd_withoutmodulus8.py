#input a number from user for check even or odd without using modulus operator
num = int(input("Enter a number: "))
# Check if the number is even or odd using bitwise AND operator
if num & 1:
    print("The number is odd.")
else:
    print("The number is even.")
    
'''# Output:
Enter a number: 4
The number is even.'''