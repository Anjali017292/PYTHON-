# Check if a string is a palindrome
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Test the function with a sample string
test_string = "A man, a plan, a canal: Panama"
# The function removes non-alphanumeric characters and converts the string to lowercase before checking if it reads the same forwards and backwards.
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")

'''
Output:
'A man, a plan, a canal: Panama' is a palindrome.
'''