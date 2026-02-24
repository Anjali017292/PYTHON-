# Generate Fibonacci series up to N using while loop
# Input a number N and generate Fibonacci series up to N
n = int(input("Enter a number: "))

# Initialize first two numbers of the Fibonacci series
a, b = 0, 1

# Print the first number of the series
print(a, end=" ")

# Generate and print the rest of the Fibonacci series up to N
while b <= n:
    print(b, end=" ")
    a, b = b, a + b

print()  # Print a newline at the end

'''#output:
    Enter a number: 20
    0 1 1 2 3 5 8 13 '''