# q7_numbers_greater_than_10.py
# Find numbers greater than 10

import numpy as np

numbers = np.arange(1, 16)

result = numbers[numbers > 10]

print("Numbers greater than 10:")
print(result)

'''output
Numbers greater than 10:
[11 12 13 14 15]'''