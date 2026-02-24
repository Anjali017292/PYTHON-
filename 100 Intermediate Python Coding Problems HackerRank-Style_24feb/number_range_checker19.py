#Number range checker
#input a number from user
# Number Range Checker

number = int(input("Enter a number: "))
#check if the number is within the range of 1 to 100
if 1 <= number <= 100:
    print("Number is within the range (1–100)")
else:
    print("Number is outside the range (1–100)")
    
'''#Output:
Enter a number: 50
Number is within the range (1–100)

Enter a number: 150
Number is outside the range (1–100)'''