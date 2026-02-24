#input two sets and check if the first is a subset of the second
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
#display the sets and whether the first is a subset of the second
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
#display whether the first is a subset of the second
print(f"Is set1 a subset of set2: {is_subset}")

'''
Output:
Set 1: {1, 2, 3}
Set 2: {1, 2, 3, 4, 5}
Is set1 a subset of set2: True
'''