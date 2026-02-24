#input two lists of numbers and find the common elements between them
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []
#using a for loop to iterate through the first list and check if each element is in the second list
for num in list1:
    if num in list2:
        common_elements.append(num)
        #display the current number and its presence in both lists
print(f"List 1: {list1}")
#display the second list
print(f"List 2: {list2}")
#display the common elements between the two lists
print(f"Common elements: {common_elements}")

'''
Output:
List 1: [1, 2, 3, 4, 5]
List 2: [4, 5, 6, 7, 8]
Common elements: [4, 5]
'''