import numpy as np

# create 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# transpose means rows become columns
transpose = matrix.T

# print result
print("Transpose:\n", transpose)


'''Output:
Transpose:
 [[1 4]
 [2 5]
 [3 6]]
'''