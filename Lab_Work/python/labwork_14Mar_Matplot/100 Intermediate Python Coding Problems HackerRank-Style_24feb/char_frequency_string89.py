# Count the frequency of each character in a string
text = "Hello, World!"
char_count = {}
# The function iterates through each character in the string and uses a dictionary to count the occurrences of each character. The get() method is used to handle characters that are not yet in the dictionary, initializing their count to 0 before incrementing.
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print("Character frequencies:")
# Finally, the code prints the frequency of each character in the string.
for char, count in char_count.items():
    print(f"'{char}': {count}")

'''
Output:
Character frequencies:
'H': 1
'e': 1
'l': 3
'o': 2
',': 1
' ': 1
'W': 1
'r': 1
'd': 1
'!': 1
'''