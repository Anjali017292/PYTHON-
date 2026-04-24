# Take a number as input from the user
num = int(input("Enter a number: "))

# Store the sign of the number
# If the number is negative, sign = -1, otherwise sign = 1
sign = -1 if num < 0 else 1

# Convert the number to positive for processing
num = abs(num)

# Variable to store the reversed number
reversed_num = 0

# Loop to reverse the number
while num > 0:
    digit = num % 10            # Extract the last digit
    reversed_num = reversed_num * 10 + digit   # Add digit to reversed number
    num //= 10                  # Remove the last digit

# Multiply with sign to restore original sign
print("The reversed number is:", sign * reversed_num)

'''# Output:
Enter a number: -1234
The reversed number is: -4321'''