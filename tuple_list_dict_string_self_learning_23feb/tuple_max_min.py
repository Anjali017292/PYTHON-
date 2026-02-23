# Input numbers and store them in a tuple
t = tuple(map(int, input("Enter numbers separated by space: ").split()))

print("Tuple:", t)

print("Maximum number:", max(t))
print("Minimum number:", min(t))

'''# Output:
Enter numbers separated by space: 5 8 2 10 3
Tuple: (5, 8, 2, 10, 3)
Maximum number: 10
Minimum number: 2'''