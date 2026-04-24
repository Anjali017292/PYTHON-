# Find the first non-repeating character in a string
s = "aabbcde"

# loop through string
for ch in s:
    # count occurrence of each character
    if s.count(ch) == 1:
        # display first non-repeating character
        print("First non-repeating:", ch)
        break
    
'''# Output:
First non-repeating: c 
# Note: 'c' is the first non-repeating character in the string "aabbcde"
'''