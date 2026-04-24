# q6_row_column_sum.py
# Calculate row-wise and column-wise sum

import numpy as np

matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])

row_sum = np.sum(matrix, axis=1)
column_sum = np.sum(matrix, axis=0)

print("Row Sum:")
print(row_sum)

print("Column Sum:")
print(column_sum)


'''output
Row Sum:
[10 26 42 58]
Column Sum:
[28 32 36 40]
'''