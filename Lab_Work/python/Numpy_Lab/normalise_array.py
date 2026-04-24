# q9_normalize_array.py
# Normalize random numbers between 0 and 1

import numpy as np

random_array = np.random.rand(10)

normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))

print("Original Array:")
print(random_array)

print("Normalized Array:")
print(normalized_array)


'''output
Original Array:
[0.17966985 0.60103874 0.88750798 0.59315957 0.82996892 0.80467465
 0.60376606 0.70912929 0.07943584 0.6704923 ]
Normalized Array:
[0.12404092 0.64549052 1.         0.63573994 0.92879465 0.89749266
 0.6488656  0.77925401 0.         0.73144022]
 '''