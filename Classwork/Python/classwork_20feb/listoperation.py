#creating list of numbers
numbers=[45,47,89,34,56]

#display the list 
print("-----------------------------------------")
print("Numbers are:",numbers)

#display data without square brackets
print("-----------------------------------------")
print("Numbers are:")
print(*numbers)

#display elements by using for loop 
print("------------------------------------")
print("numbers are:")
for num in numbers:
    print(num)
    

length=len(numbers)
print("-----------------------------------------")
print("number of elements in list:",length)

print("-------------------------------")
print("Numbers in reverse order:")
for index in range(length-1,-1,-1):
    print(numbers[index],end=",")
    
#find sum of all numbers in list
print("-----------------------------------------")
sum=0
for i in numbers:
    sum=sum+i;
print("Sum of all numbers in the  list",sum)

#finding greatest number in list
print("-----------------------------------------")
max=numbers[0]
for index in range(1,length):
    if(max < numbers[index]):
        max=numbers[index]
print("Maximun number in the list is :",max)


#output:-----------------------------------------
#Numbers are: [45, 47, 89, 34, 56]
#-----------------------------------------
#Numbers are:45 47 89 34 56
#------------------------------------
#numbers are:
#45
#47
#89
#34
#56
#-----------------------------------------
#number of elements in list: 5
#-------------------------------
#Numbers in reverse order:56,34,89,47,45,
#-----------------------------------------
#Sum of all numbers in the  list: 271
#-----------------------------------------
#Maximun number in the list is : 56

