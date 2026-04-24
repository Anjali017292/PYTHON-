# Count the number of words in a sentence
sentence = "The quick brown fox jumps over the lazy dog."
# The function splits the sentence into words using the split() method and counts the number of words by taking the length of the resulting list.
word_count = len(sentence.split())
print(f"Number of words in the sentence: {word_count}")

'''
Output:
Number of words in the sentence: 9
'''