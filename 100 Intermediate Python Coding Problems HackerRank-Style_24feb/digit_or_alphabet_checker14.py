#input a character from user for checking whether it is digit or alphabet
char = input("Enter a character: ")
#check whether the character is digit or alphabet using if-elif-else statements
if char.isdigit():
    print("The character is a digit.")
elif char.isalpha():
    print("The character is an alphabet.")
else:
    print("The character is neither a digit nor an alphabet.")
    
#output of the program is shown below:
'''Output:
Enter a character: 5    
The character is a digit.
Enter a character: A
The character is an alphabet.
Enter a character: @
The character is neither a digit nor an alphabet.'''