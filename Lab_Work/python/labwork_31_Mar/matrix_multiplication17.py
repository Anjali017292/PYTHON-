import numpy as np

# create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# perform matrix multiplication
# dot() multiplies rows with columns
result = np.dot(A, B)

# print result
print("Matrix Multiplication:\n", result)


'''Output:
Matrix Multiplication:
 [[19 22]
 [43 50]]
'''