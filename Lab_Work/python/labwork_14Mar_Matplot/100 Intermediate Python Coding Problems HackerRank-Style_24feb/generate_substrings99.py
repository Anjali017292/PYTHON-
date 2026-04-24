# Generate all substrings of a given string
original_string = "abc"
substrings = []

for i in range(len(original_string)):
    for j in range(i + 1, len(original_string) + 1):
        substrings.append(original_string[i:j])

print(f"Original string: {original_string}")
print(f"All substrings: {substrings}")

'''
Output:
Original string: abc
All substrings: ['a', 'ab', 'abc', 'b', 'bc', 'c']
'''