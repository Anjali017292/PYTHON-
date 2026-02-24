#input a number and print its factorial using while loop
# Input a number and print its factorial using while loop

def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

number = int(input("Enter a number: "))
print("Factorial of", number, "is", factorial(number))


'''#output:
    Enter a number: 5
    Factorial of 5 is 120'''