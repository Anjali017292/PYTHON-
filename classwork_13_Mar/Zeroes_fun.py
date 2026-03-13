import numpy as np
#creating an array
numbers1=np.array([45,78,90])
print("Array:")
print(numbers1)
print("------------------")
#creating zeros array
array1=np.zeros((3,4))
print("Zeros array of order (3,4) :")
print(array1)
print("------------------")
#zeros array
array2=np.zeros((5,3),dtype=int)
print("Zeros array of order (5,3) :")
print(array2)
print("------------------")

'''output
Array:
[45 78 90]
------------------
Zeros array of order (3,4) :
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
 ------------------
Zeros array of order (5,3) :
[[0 0 0]
 [0 0 0]
 [0 0 0]
 [0 0 0]
 [0 0 0]]
------------------
'''