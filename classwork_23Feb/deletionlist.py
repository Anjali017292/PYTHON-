#create a list of 10 elements with repeated numbers 
numbers = [45,47,89,45,67,89,45,23,67,89]
#display the list
print("numbers are:")
print(numbers)
print("-------------------------------------")
#to delete element at index 5
numbers.pop(5)
print("after deleting element at index 5:")
print(numbers)
numbers.pop()
print("after deleting last element:")
print(numbers)

#to delete 45
numbers.remove(45)
print("after deleting 45:")
print(numbers)

#to delete 45
numbers.remove(45)
print("after deleting 45:")
print(numbers)

'''#output:
numbers are: [45, 47, 89, 45, 67, 89, 45, 23, 67, 89]
after deleting element at index 5: [45, 47, 89, 45, 67, 45, 23, 67, 89]
after deleting last element: [45, 47, 89, 45, 67, 45, 23, 67]
after deleting 45: [47, 89, 45, 67, 45, 23, 67]
after deleting 45: [47, 89, 67, 45, 23, 67]
'''


