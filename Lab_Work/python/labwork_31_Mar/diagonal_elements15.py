import numpy as np

# create 2D matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# extract diagonal elements (1,5,9)
diagonal = np.diag(matrix)

# print result
print("Diagonal Elements:", diagonal)

'''Output:
Diagonal Elements: [1 5 9]
'''