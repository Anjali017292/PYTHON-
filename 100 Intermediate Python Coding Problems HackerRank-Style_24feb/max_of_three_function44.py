#input three numbers and find the maximum of the three using a function
def max_of_three(a, b, c):
    return max(a, b, c)

#call the max_of_three function and print the result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
result = max_of_three(num1, num2, num3)

#display the maximum of the three numbers
print(f"The maximum of {num1}, {num2}, and {num3} is {result}.")

'''
Output:
Enter first number: 10
Enter second number: 20
Enter third number: 30
The maximum of 10, 20, and 30 is 30.
'''