#input a number by user for checking
number = int(input("Enter a number: "))

#check the number using conditional statement
if number >= 0:
    if number == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")
