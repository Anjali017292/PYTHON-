# Taking list input
nums = list(map(int, input("Enter numbers: ").split()))

# Convert list to tuple
t = tuple(nums)

total = sum(t)

print("Tuple:", t)
print("Sum of elements:", total)

'''# Output:Enter numbers: 4 6 8 2
Tuple: (4, 6, 8, 2)
Sum of elements: 20'''