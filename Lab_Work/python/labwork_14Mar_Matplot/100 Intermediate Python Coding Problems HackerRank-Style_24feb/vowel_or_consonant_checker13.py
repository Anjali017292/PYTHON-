#input a character from user for checking whether it is vowel or consonant
char = input("Enter a character: ")
#check whether the character is vowel or consonant
if len(char) != 1:
    print("Please enter a single character.")
elif char in 'aeiouAEIOU':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print(f"{char} is not an alphabetic character.")
    
    
'''#output
Enter a character: a
a is a vowel.
Enter a character: b
b is a consonant.
Enter a character: 1
1 is not an alphabetic character.'''
