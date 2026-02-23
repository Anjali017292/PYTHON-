# ------------------------
#List function in python
#-------------------------
#count(x) - returns the number of times x appears in the list
#reverse(x) - reverses the order of the list
#create a list of 20 numbers given by user

numbers = []

# Take 20 numbers from user
print("Enter 20 numbers:")
for i in range(20):
    num = int(input(" "))
    numbers.append(num)
#display the list
print("--------------------------------")
print()
remove_num = int(input("Enter a number to remove from the list: "))
#------------------------------------------
print("List is :")
print(numbers)
print("--------------------------------")
#frequency of the number in the list
frequency = numbers.count(remove_num)
if(frequency==0):
    print(remove_num,"is not present in the list")
elif(frequency==1):
    print("As it is unique so,cannot be removed from list")
else:
    #to reverse the list
    numbers.reverse()
    for i in range(1,frequency):
        numbers.remove(remove_num)
        numbers.reverse()
print("the list after removing:",remove_num,"List")
print(numbers)
        
        
'''#output:
Enter 20 numbers:
    45
    67
    89
    45
    67
    89
    45
    23
    67
    89
    45
    67
    89
    45
    23
    67
    89
    45
    67
    89
    
Enter a number to remove from the list: 45
List is :
[45, 67, 89, 45, 67, 89, 45, 23, 67, 89, 45, 67, 89, 45, 23, 67, 89, 45, 67, 89]
the list after removing: 45 List
[67, 89, 67, 89, 23, 67, 89, 67, 89]

'''