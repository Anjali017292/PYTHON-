# Count digits in a number using while loop

number = int(input("Enter a number: "))
# Count digits in the number using while loop
n = abs(number)
count = 0
# If the number is 0, it has 1 digit
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1
# Output the total number of digits
print("Total digits:", count)


'''#output:
    Enter a number: 12345
    Total digits: 5'''