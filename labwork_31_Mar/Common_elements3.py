l1 = [1, 2, 3]
l2 = [2, 3, 4]

result = []

# check each element
for i in l1:
    if i in l2:              # if present in second list
        if i not in result:  # avoid duplicates
            result.append(i)
# display result
print(result)

'''# Output:
[2, 3]
'''