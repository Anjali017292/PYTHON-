# Count uppercase and lowercase letters in a string
original_string = "Hello, World!"
uppercase_count = 0
lowercase_count = 0

for char in original_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print(f"Original string: {original_string}")
print(f"Uppercase count: {uppercase_count}")
print(f"Lowercase count: {lowercase_count}")

'''
Output:
Original string: Hello, World!
Uppercase count: 2
Lowercase count: 8
'''