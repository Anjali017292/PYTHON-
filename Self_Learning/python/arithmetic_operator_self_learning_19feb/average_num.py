n = int(input("Enter how many numbers: "))
total = 0

for i in range(n):
    num = float(input("Enter number: "))
    total += num

average = total / n
print("Average =", average)
