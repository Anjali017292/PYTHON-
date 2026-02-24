# Calculate power of a number without using ** operator
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(exponent):
    result *= base
print("Result:", result)
'''Output:
Enter the base: 2
Enter the exponent: 5
Result: 32'''