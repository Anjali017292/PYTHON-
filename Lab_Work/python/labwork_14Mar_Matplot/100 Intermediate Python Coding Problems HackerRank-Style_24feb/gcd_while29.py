# Find GCD of two numbers using while loop
# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Store original values for output
original_a, original_b = a, b
# Find GCD using while loop
while b != 0:
    a, b = b, a % b
# Print the GCD
print(f"GCD of {original_a} and {original_b} is {a}")

'''#output:
    Enter first number: 12
    Enter second number: 18
    GCD is 6'''