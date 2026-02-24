# Remove all spaces from a string
original_string = "Hello, World! This is a test string."
# The function removes all spaces from the original string using the replace() method.
no_spaces_string = original_string.replace(" ", "")

# Finally, the code prints the original string and the string without spaces.
print(f"Original string: {original_string}")
print(f"String without spaces: {no_spaces_string}")

'''
Output:
Original string: Hello, World! This is a test string.
String without spaces: Hello,World!Thisisateststring.
'''