# Reverse a number using while loop
# Input a number and reverse it using while loop
number = int(input("Enter a number: "))

# Reversing the number using while loop
n = number
reverse = 0
# Loop to reverse the number
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
# Output the reversed number
print("Reversed number is:", reverse)

'''#output:
    Enter a number: 12345
    Reversed number is: 54321'''