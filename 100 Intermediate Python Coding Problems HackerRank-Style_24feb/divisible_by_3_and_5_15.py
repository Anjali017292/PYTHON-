#input a number by user to check whether it is divisible by 3 and 5 or not
num = int(input("Enter a number: "))
#check whether the number is divisible by 3 and 5 using if-elif-else
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 but not by 5.")
elif num % 5 == 0:
    print(f"{num} is divisible by 5 but not by 3.")
else:
    print(f"{num} is not divisible by either 3 or 5.")

#output of the program is shown below:
'''Output:
Enter a number: 15
15 is divisible by both 3 and 5.
Enter a number: 9
9 is divisible by 3 but not by 5.
Enter a number: 10
10 is divisible by 5 but not by 3.
Enter a number: 7
7 is not divisible by either 3 or 5.'''