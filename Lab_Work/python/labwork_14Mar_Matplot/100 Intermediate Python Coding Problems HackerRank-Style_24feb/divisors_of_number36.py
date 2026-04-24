#input a number and find the divisors of that number
num = int(input("Enter a number: "))
# find the divisors of the number
print("The divisors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i,end=" ")
        
'''
Output:
Enter a number: 36
The divisors of 36 are:
1 2 3 4 6 9 12 18 36   
'''
        