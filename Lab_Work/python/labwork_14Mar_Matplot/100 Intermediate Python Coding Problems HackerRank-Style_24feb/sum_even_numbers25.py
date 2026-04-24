# Find sum of even numbers up to N using while loop
# Input a number and find the sum of even numbers up to that number using while loop
n = int(input("Enter a number: "))

i = 1
total = 0
# Loop to find the sum of even numbers up to N
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
# Output the sum of even numbers
print("Sum of even numbers:", total)

'''#output:
    Enter a number: 10
    Sum of even numbers: 30'''
    