# q10_reverse_array.py
# Reverse a NumPy array

import numpy as np

numbers = np.arange(1, 11)

reversed_array = numbers[::-1]

print("Reversed Array:")
print(reversed_array)

'''output
Reversed Array:
[10  9  8  7  6  5  4  3  2  1]
'''