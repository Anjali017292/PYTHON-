# Replace vowels in a string with stars
original_string = "Hello, World!"
vowels = "aeiouAEIOU"
# The function iterates through each character in the original string and replaces vowels with stars.
modified_string = ''.join('*' if char in vowels else char for char in original_string)
print(f"Original string: {original_string}")
print(f"Modified string: {modified_string}")

'''
Output:
Original string: Hello, World!
Modified string: H*ll*, W*rld!
'''