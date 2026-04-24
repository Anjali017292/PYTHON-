# Find the longest word in a sentence
sentence = "The quick brown fox jumps over the lazy dog."
words = sentence.split()
# The function splits the sentence into words using the split() method and finds the longest word by using the max() function with the key parameter set to len, which returns the length of each word. Finally, the code prints the longest word.
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")

'''
Output:
Longest word: quick
'''