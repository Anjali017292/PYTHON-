#list of five numbers
list1=[45,47,89,34,56]
#display the list
print("Numbers are:",list1)
print("-----------------------------------------")
#inserting 150 at the end of the list
list1.append(150)
print("After inserting 150 at the end of the list:",list1)
print("-----------------------------------------")
#inserting a list of five numbers at the end of the list
list2=[23,45,67,89,90]
list1.extend(list2)
print("list2 is:",list2)
print("After inserting list2 at the end of list1:",list1)
print("-----------------------------------------")

#inserting at particular index
list1.insert(2,100)
print("After inserting 100 at index 2:",list1)
print("-----------------------------------------")






'''output:-----------------------------------------
Numbers are: [45, 47, 89, 34, 56]
After inserting 150 at the end of the list: [45, 47, 89, 34, 56, 150]
list2 is: [23, 45, 67, 89, 90]
After inserting list2 at the end of list1: [45, 47, 89, 34, 56, 150, 23, 45, 67, 89, 90]
-----------------------------------------
After inserting 100 at index 2: [45, 47, 100, 89, 34, 56, 150, 23, 45, 67, 89, 90]'''