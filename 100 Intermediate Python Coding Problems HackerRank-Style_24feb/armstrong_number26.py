# Program to check whether a number is an Armstrong number

# Input number from the user
num = int(input("Enter a number: "))

# Initialize sum variable
total = 0

# Store the original number to compare later
temp = num

# Find number of digits in the number
digits = len(str(num))

# Calculate the sum of each digit raised to the power of total digits
while temp > 0:
    digit = temp % 10        # Get last digit
    total += digit ** digits # Add power of digit to total
    temp //= 10              # Remove last digit

# Check Armstrong condition
if num == total:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
    
'''#output:
    Enter a number: 153
    153 is an Armstrong number'''