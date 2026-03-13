# q4_matrix_multiplication.py
# Perform matrix multiplication of two 3x3 matrices

import numpy as np

matrix_A = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])

matrix_B = np.array([[9,8,7],
                     [6,5,4],
                     [3,2,1]])

result = np.dot(matrix_A, matrix_B)

print("Result Matrix Multiplication is:")
print(result)

'''output
Result Matrix Multiplication is:
[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
'''