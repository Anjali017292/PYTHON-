# Remove duplicate from list
lst = [1, 2, 2, 3, 4, 3]
result = []

# loop through list
for i in lst:
    # check if element is not in result
    if i not in result:   # check duplicate
        result.append(i)
#display result
print(result)

'''# Output:
[1, 2, 3, 4]
# Note: The duplicate elements '2' and '3' are removed from the list.
'''