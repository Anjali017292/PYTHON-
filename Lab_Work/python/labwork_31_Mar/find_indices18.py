import numpy as np

# create array
arr = np.array([10, 25, 30, 5, 15])

# given value
value = 20

# find indices where element > value
indices = np.where(arr > value)

# print indices
print("Indices:", indices)


'''Output:
Indices: (array([1, 2]),)
'''