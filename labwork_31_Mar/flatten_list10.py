# Flatten a nested list
lst = [1, [2, [3, 4], 5], 6]
# Flatten the list
result = []

# loop through list
for i in lst:
    if type(i) == list:   # check if element is list
        for j in i:
            if type(j) == list: # check if element is list
                for k in j:
                    result.append(k)
            else:
                result.append(j)
    else:
        result.append(i)
#display result
print(result)

'''# Output:
[1, 2, 3, 4, 5, 6]
# Note: The nested list [2, [3, 4], 5] is flattened to individual elements in the result list.
'''