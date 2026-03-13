# q5_middle_submatrix.py
# Extract the middle 3x3 matrix from a 5x5 matrix

import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)

middle_matrix = matrix[1:4, 1:4]

print("Middle 3x3 Matrix:")
print(middle_matrix)

'''output
Middle 3x3 Matrix:
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
 '''