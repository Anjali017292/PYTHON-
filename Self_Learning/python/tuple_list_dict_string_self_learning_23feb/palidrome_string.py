# Program to check palindrome
# This program prompts the user to enter a string and then checks if the string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). 
# The program reverses the input string and compares it to the original string. 
# If they are the same, it prints "Palindrome"; otherwise, it prints "Not Palindrome".
text = input("Enter a string: ")

#its a string in reverse order
rev = text[::-1]

#its checks the original string and reversed string are same or not
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    
'''#output
Enter a string: madam
Palindrome
Enter a string: hello
Not Palindrome'''