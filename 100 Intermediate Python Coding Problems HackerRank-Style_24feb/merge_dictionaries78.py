# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Method 1: Using the unpacking operator (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(f"Merged dictionary: {merged_dict}")

'''
Output:
Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''