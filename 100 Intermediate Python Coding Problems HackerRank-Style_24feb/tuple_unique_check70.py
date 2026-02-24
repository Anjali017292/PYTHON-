#input a tuple of numbers and check if all elements are unique
numbers = (1, 2, 3, 4, 5)
is_unique = len(numbers) == len(set(numbers))
#display the tuple and whether all elements are unique or not
print(f"Tuple: {numbers}")
#display whether all elements are unique or not
print(f"All elements unique: {is_unique}")

'''
Output:
Tuple: (1, 2, 3, 4, 5)
All elements unique: True
'''