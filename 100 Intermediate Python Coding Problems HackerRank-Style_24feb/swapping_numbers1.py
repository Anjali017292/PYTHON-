# Input two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap without using a third variable
a = a + b
b = a - b
a = a - b

# Output the swapped numbers
print("After swapping:")
print("First number:", a)
print("Second number:", b)

'''# Output:
Enter first number: 5
Enter second number: 10
After swapping:
First number: 10
Second number: 5'''