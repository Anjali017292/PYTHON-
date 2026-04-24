# Input a number and print its factorial using a for loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

'''#output:
    Enter a number: 5
    Factorial of 5 is 120'''