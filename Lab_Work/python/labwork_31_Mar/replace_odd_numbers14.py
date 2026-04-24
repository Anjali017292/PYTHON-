import numpy as np # import numpy library

# create array
arr = np.array([1, 2, 3, 4, 5, 6])

# condition: if number is odd (not divisible by 2)
# replace those values with -1
arr[arr % 2 != 0] = -1

# print modified array
print("Modified Array:", arr)


'''Output:
Modified Array: [-1  2 -1  4 -1  6]
'''