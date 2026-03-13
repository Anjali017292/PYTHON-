import numpy as np
#creating array
numbers1=np.array([45,78,90])
print("Array: ")
print(numbers1)
print("------------------")
#second array
numbers2=np.array([45,3.5,90])
print("Second Array: ")
print(numbers2)
print("------------------")
#third array
numbers3=np.array([45,3.5,90,'hello'])
print("Third Array: ")
print(numbers3)
print("------------------")
#multiply each element by 3
print("After mulitply by 3:")
print(numbers1*3)
print("------------------")
#element greater than 70
print("Element > 70 :")
print(numbers1>70)
print("------------------")
#double dimension array
matrix1=np.array([[45,67,89],[56,90,67]])
print("2D array :")
print(matrix1)
print("------------------")
#3D array
matrix2=np.array([[45,67,89],[56,90,67],[34,56,78]])
print("3D array:")
print(matrix2)
print("------------------")


'''output
Array: 
[45 78 90]
------------------
Second Array: 
[45.   3.5 90. ]
------------------
Third Array: 
['45' '3.5' '90' 'hello']
------------------
After mulitply by 3:
[135 234 270]
------------------
Element > 70 :
[False  True  True]
------------------
2D array :
[[45 67 89]
 [56 90 67]]
------------------
3D array:
[[45 67 89]
 [56 90 67]
 [34 56 78]]
------------------
'''
