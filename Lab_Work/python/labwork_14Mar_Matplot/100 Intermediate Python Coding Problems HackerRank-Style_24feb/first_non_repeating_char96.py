# Find the first non-repeating character in a string
original_string = "programming"
char_count = {}
# Count occurrences of each character
for char in original_string:
    char_count[char] = char_count.get(char, 0) + 1
# Find the first non-repeating character
first_non_repeating_char = None
for char in original_string:
    if char_count[char] == 1:
        first_non_repeating_char = char
        break

print(f"Original string: {original_string}")
print(f"First non-repeating character: {first_non_repeating_char}")

'''
Output:
Original string: programming
First non-repeating character: p
'''