#  input a number from user and calculate the sum of its digits
num = int(input("Enter a number: "))
# Handle negative numbers by taking the absolute value
num = abs(num)

# Initialize sum of digits
digit_sum = 0
# Calculate the sum of digits
while num > 0:
    digit_sum += num % 10
    num //= 10
# Output the sum of digits
print("The sum of the digits is:", digit_sum)

'''# Output:
Enter a number: 1234
The sum of the digits is: 10'''