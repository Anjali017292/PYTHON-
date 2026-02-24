#input a number and calculate the sum of its digits using a function
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

#call the sum_of_digits function and print the result
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}.")

'''
Output:
Enter a number: 123
The sum of digits of 123 is 6.
Enter a number: 456
The sum of digits of 456 is 15.
'''