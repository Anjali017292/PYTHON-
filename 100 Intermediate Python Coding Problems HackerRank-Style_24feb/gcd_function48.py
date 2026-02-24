#input two numbers and find their GCD using a function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#call the gcd function and print the result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {result}")

'''
Output:
Enter first number: 12
Enter second number: 18
GCD of 12 and 18 is: 6
'''