# q8_matrix_transpose.py
# Calculate transpose of a matrix

import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

transpose_matrix = matrix.T

print("Transpose Matrix:")
print(transpose_matrix)

'''output
Transpose Matrix:
[[1 4 7]
 [2 5 8]
 [3 6 9]]
 '''