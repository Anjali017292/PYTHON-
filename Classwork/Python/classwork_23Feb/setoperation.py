set1={45,67,89,34,78}
print("set1 is:")
print(set1)
print("--------------------------------")
set2={45,67,39,23,56}
print("set2 is:")
print(set2)
print("--------------------------------")
#to find union of set1 and set2
set3=set1.union(set2)
print("union of set1 and set2 is:")
print(set3)
print("--------------------------------")
#to find intersection of set1 and set2
set4=set1.intersection(set2)
print("intersection of set1 and set2 is:")
print(set4)
print("--------------------------------")


'''#output:
set1 is:
{67, 34, 78, 45, 89}
set2 is:
{67, 39, 23, 45, 56}
union of set1 and set2 is:
{67, 34, 78, 45, 89, 39, 23, 56}
intersection of set1 and set2 is:
{67, 45}
'''