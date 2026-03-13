# q2_random_matrix_min_max.py
# Create a 5x5 matrix with random integers and find minimum and maximum value

import numpy as np

matrix = np.random.randint(1, 101, (5, 5))  # random integers 1-100

print("Matrix is:")
print(matrix)

minimum_value = np.min(matrix)
maximum_value = np.max(matrix)

print("Min =", minimum_value)
print("Max =", maximum_value)

'''output
Matrix is:
[[85 15 73 47  1]
 [62 46 40  3 93]
 [77 42 58 70 84]
 [20 33 54 38 13]
 [91 92 36 69 26]]
Min = 1
Max = 93
'''