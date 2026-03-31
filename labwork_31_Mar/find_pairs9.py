# Find pairs in list that sum to target
lst = [1, 2, 3, 4, 5]
# target sum
target = 5

# check all pairs
for i in range(len(lst)):
    # check if sum of pair is equal to target
    for j in range(i + 1, len(lst)):
        # if sum of pair is equal to target
        if lst[i] + lst[j] == target:
            # print the pair
            print(lst[i], lst[j])
            
'''# Output:
1 4
2 3
# Note: The pairs (1, 4) and (2, 3) sum to the target value of 5.
'''