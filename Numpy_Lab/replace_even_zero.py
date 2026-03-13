# q3_replace_even_zero.py
# Replace even numbers with 0

import numpy as np

numbers = np.arange(1, 11)  # array from 1 to 10

numbers[numbers % 2 == 0] = 0   # replace even numbers

print("Modified Array:")
print(numbers)

'''output
Modified Array:
[1 0 3 0 5 0 7 0 9 0]
'''