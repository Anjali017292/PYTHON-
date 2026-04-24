# input string
s = "hello"

# empty dictionary
freq = {}

# loop through characters
for ch in s:
    if ch in freq:
        freq[ch] += 1   # increase count
    else:
        freq[ch] = 1    # first occurrence
# display frequency
print(freq)

'''# Output:
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
