import numpy as np

# create array
arr = np.array([10, 20, 30, 40, 50])

# find minimum and maximum values
min_val = np.min(arr)
max_val = np.max(arr)

# apply normalization formula
# (value - min) / (max - min)
normalized = (arr - min_val) / (max_val - min_val)

# print normalized values
print("Normalized Array:", normalized)


'''Output:
Normalized Array: [0.   0.25 0.5  0.75 1.  ]
'''