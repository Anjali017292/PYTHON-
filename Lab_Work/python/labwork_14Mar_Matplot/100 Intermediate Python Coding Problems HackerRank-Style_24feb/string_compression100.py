# String compression - compress a string by counting repeated characters
original_string = "aabcccccaaa"
compressed_string = ""
current_char = original_string[0]
char_count = 1
# The function iterates through the original string, counting consecutive characters. When it encounters a different character, it appends the current character and its count to the compressed string and resets the count for the new character.
for i in range(1, len(original_string)):
    if original_string[i] == current_char:
        char_count += 1
    else:
        compressed_string += current_char + str(char_count)
        current_char = original_string[i]
        char_count = 1

# Append the last character and its count
compressed_string += current_char + str(char_count)

print(f"Original string: {original_string}")
print(f"Compressed string: {compressed_string}")

'''
Output:
Original string: aabcccccaaa
Compressed string: a2b1c5a3
'''