# Reverse a string without using slicing
original_string = "Hello, World!"
reversed_string = ""
# Iterate through each character in the original string and prepend it to the reversed string
for char in original_string:
    reversed_string = char + reversed_string
    # This way, each new character is added to the front of the reversed string, effectively reversing it.
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")

'''
Output:
Original string: Hello, World!
Reversed string: !dlroW ,olleH
'''