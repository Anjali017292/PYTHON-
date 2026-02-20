#creating a blank list
numbers = []
#taking input from user and adding to the list
n=int(input("Enter number of elements in the list:"))
for i in range(n):
    num=int(input())
    print("------------------------")
    numbers.append(num)
#displaying the list
print("Numbers in the list are:")
print(numbers)

#find sum of all numbers in list
print("-----------------------------------------")
sum=0
for i in numbers:
    sum=sum+i;
print("Sum of all numbers in the list is:",sum)

#output:Enter number of elements in the list:5
#45
#47
#89
#34
#56
#------------------------
#------------------------
#------------------------
#Numbers in the list are:
#[45, 47, 89, 34, 56]
#-----------------------------------------
#Sum of all numbers in the list is: 271
