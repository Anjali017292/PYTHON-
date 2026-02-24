# Remove duplicate characters from a string
original_string = "programming"
# The function removes duplicate characters from the original string by converting it to a set of characters (which automatically removes duplicates) and then back to a string.
unique_chars_string = ''.join(set(original_string))
print(f"Original string: {original_string}")
print(f"String with unique characters: {unique_chars_string}")

'''
Output:
Original string: programming
String with unique characters: progamin
'''