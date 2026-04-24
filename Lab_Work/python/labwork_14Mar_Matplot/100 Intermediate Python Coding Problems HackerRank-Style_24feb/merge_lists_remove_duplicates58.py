#input two lists of numbers and merge them, then remove duplicates from the merged list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list1 + list2
unique_list = []
#using a for loop to iterate through the merged list and append each unique element to the unique_list
for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)
        #display the current number and its uniqueness
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged list: {merged_list}")
print(f"List after removing duplicates: {unique_list}")

'''
Output:
List 1: [1, 2, 3, 4, 5]
List 2: [4, 5, 6, 7, 8]
Merged list: [1, 2, 3, 4, 5, 4, 5, 6, 7, 8]
List after removing duplicates: [1, 2, 3, 4, 5, 6, 7, 8]
'''