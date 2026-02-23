numbers = (10, 20, 30, 20, 40, 20, 50)

search = int(input("Enter number to count: "))

count = numbers.count(search)

print("Tuple:", numbers)
print("Occurrence of", search, "=", count)

'''# Output:
Enter number to count: 20
Tuple: (10, 20, 30, 20, 40, 20, 50)
Occurrence of 20 = 3'''