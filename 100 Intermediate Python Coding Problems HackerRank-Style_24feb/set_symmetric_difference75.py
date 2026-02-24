#input two sets and find their symmetric difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_difference_set = set1.symmetric_difference(set2)
#display the sets and their symmetric difference
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
#display the symmetric difference of the two sets
print(f"Symmetric Difference: {symmetric_difference_set}")

'''
Output:
Set 1: {1, 2, 3, 4, 5}
Set 2: {4, 5, 6, 7, 8}
Symmetric Difference: {1, 2, 3, 6, 7, 8}
'''