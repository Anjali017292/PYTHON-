#change file name set in python
set = {45,67,89,45,67,89,45,23,67,89}
print("set is:")
print(set)
print("--------------------------------")
#to insert 34 in set
set.add(34)
print("after inserting 34 in set:")
print(set)

#create empty set
set6=set()
print(type(set6))
set6.add(46)
set6.add(78)
print("set6 is:")   
print(set6)



'''#output:
set is:
{67, 89, 45, 23}
after inserting 34 in set:
{67, 34, 89, 45, 23}
set6 is:
{46, 78}
'''