# q1_matrix_reshape.py
# Create a NumPy array from 1 to 20 and reshape it into a 4x5 matrix

import numpy as np

numbers = np.arange(1, 21)   # array from 1 to 20
matrix = numbers.reshape(4, 5)   # reshape into 4x5 matrix

print("4x5 Matrix:")
print(matrix) 

'''output
4x5 Matrix:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]]'''