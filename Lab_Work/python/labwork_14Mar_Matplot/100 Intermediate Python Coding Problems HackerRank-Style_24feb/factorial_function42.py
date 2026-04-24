#input a number and calculate its factorial using a function
def factorial(n):
    #base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    #recursive case: factorial of n is n multiplied by factorial of (n-1)
num = int(input("Enter a number: "))
#call the factorial function and print the result
result = factorial(num)
print(f"The factorial of {num} is {result}.")

'''
Output:
Enter a number: 5
The factorial of 5 is 120.
Enter a number: 0
The factorial of 0 is 1.'''