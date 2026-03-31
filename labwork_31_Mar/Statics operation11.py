import numpy as np   # import numpy library

# create numpy array
arr = np.array([10, 20, 30, 40, 50])

# calculate mean (average)
mean = np.mean(arr)

# calculate median (middle value)
median = np.median(arr)

# calculate standard deviation (spread of data)
std = np.std(arr)

# print results
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)


'''#output
Mean: 30.0  
Median: 30.0
Standard Deviation: 14.142135623730951
'''