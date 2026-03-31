# Swap keys and values in a dictionary
d = {'a': 1, 'b': 2}
# empty dictionary to store swapped key-value pairs
new_dict = {}

# swap key and value
for key in d:
    value = d[key] # get value for current key
    new_dict[value] = key # assign key to value in new dictionary

print(new_dict)

'''# Output:
{1: 'a', 2: 'b'}
# Note: The keys and values in the original dictionary have been swapped in the new dictionary.
'''