#input two numbers and find their power using a recursive function
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

#call the power function and print the result
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

#calculate the power using the recursive function
result = power(base, exponent)
print(f"{base} raised to the power {exponent} is: {result}")

'''
Output:
Enter base: 2
Enter exponent: 3
2 raised to the power 3 is: 8
'''