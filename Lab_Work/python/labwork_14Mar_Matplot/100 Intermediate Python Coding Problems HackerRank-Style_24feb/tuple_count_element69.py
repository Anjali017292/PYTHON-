#input a tuple of numbers and count the occurrences of a specific element in the tuple
numbers = (1, 2, 3, 2, 4, 2, 5)
element = 2
count = numbers.count(element)
#display the tuple and the count of the specific element
print(f"Tuple: {numbers}")
#display the count of the specific element
print(f"Count of {element}: {count}")

'''
Output:
Tuple: (1, 2, 3, 2, 4, 2, 5)
Count of 2: 3
'''