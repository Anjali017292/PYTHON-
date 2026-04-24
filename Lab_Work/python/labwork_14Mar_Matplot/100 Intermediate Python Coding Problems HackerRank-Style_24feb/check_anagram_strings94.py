# Check if two strings are anagrams of each other
string1 = "listen"
string2 = "silent"

# Convert both strings to lowercase and sort their characters
sorted_string1 = sorted(string1.lower())
sorted_string2 = sorted(string2.lower())

# Compare the sorted strings
is_anagram = sorted_string1 == sorted_string2

print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Are they anagrams? {is_anagram}")

'''
Output:
String 1: listen
String 2: silent
Are they anagrams? True
'''