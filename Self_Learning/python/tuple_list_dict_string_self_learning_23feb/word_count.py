# Program to count words in a sentence
# This program prompts the user to enter a sentence and then counts the number of words in that sentence.
# It uses the split() method to divide the input string into a list of words based on whitespace. 
# The length of this list is then calculated using the len() function, which gives the total number of words in the sentence. 
# Finally, it prints the word count to the user.
sentence = input("Enter a sentence: ")

# The split() method is used to split the input string into a list of words. 
# By default, it splits the string based on whitespace (spaces, tabs, etc.).
words = sentence.split()

print("Number of words:", len(words))

'''#output
Enter a sentence: Hello world, welcome to Python programming!
Number of words: 6
Enter a sentence: This is a test.
Number of words: 4'''