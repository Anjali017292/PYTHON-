from numericcalculation import calculateremainder
num=int(input("Enter a number:"))
if(calculateremainder(num,2)==0):
    print(num,"is an even number")
else:
    print(num,"is an odd number")
    
'''output:
Enter a number: 10
10 is an even number
Enter a number: 15
15 is an odd number
'''