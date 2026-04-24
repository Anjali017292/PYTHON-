# Calculate the sum of first n natural numbers
n = int(input("Enter a number: "))
# Initialize sum to 0
sum = 0
# Iterate through the numbers from 1 to n and add them to sum
for i in range(1, n + 1):
    sum += i
    # sum = sum + i
print(f"Sum of first {n} natural numbers is {sum}")

'''Output:
Enter a number: 5
Sum of first 5 natural numbers is 15'''