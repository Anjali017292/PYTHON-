#input a string and check if it is a palindrome using a function
def is_palindrome(s):
    #remove spaces and convert to lowercase for comparison
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    #check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

#call the is_palindrome function and print the result
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

'''
Output:
Enter a string: racecar
'racecar' is a palindrome.
Enter a string: hello
'hello' is not a palindrome.
'''