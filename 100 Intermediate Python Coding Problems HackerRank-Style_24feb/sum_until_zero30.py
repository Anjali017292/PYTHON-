# Sum numbers until zero is entered
total = 0
# Continuously input numbers until the user enters zero
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
# Print the total sum of the numbers entered
print(f"Sum of all numbers entered is: {total}")

'''#output:
    Enter a number (0 to stop): 5
    Enter a number (0 to stop): 10
    Enter a number (0 to stop): -3
    Enter a number (0 to stop): 0
    Sum of all numbers entered is: 12'''