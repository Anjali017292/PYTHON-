# Create a dictionary to store character frequencies in a string
text = "hello world"
char_freq = {}
# Count the frequency of each character in the string
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1
print(f"Character frequencies: {char_freq}")

'''Output:
Character frequencies: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
'''