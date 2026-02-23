# Program to count vowels and consonants
# This program prompts the user to enter a string and then counts the number of vowels and consonants in that string. It uses a loop to iterate through each character in the string, checking if it is an alphabetic character. If it is, it further checks if it is a vowel (both uppercase and lowercase) or a consonant and updates the respective counts accordingly. Finally, it prints the total number of vowels and consonants found in the input string.
text = input("Enter a string: ")

# A string is a sequence of characters enclosed in quotes.
# In this program, we take input from the user and store it in the variable 'text'.
# We will then analyze this string to count the number of vowels and consonants it contains.
vowels = "aeiouAEIOU"
v = 0
c = 0

# The program defines a string 'vowels' that contains all the lowercase and uppercase vowels. It also initializes two variables 'v' and 'c' to zero, which will be used to count the number of vowels and consonants, respectively.
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
# The program uses a for loop to iterate through each character 'ch' in the input string 'text'.
# It first checks if the character is an alphabetic character using the isalpha() method. 
# If it is, it then checks if the character is in the 'vowels' string. If it is a vowel, it increments the vowel count 'v' by 1; otherwise, it increments the consonant count 'c' by 1.
print("Vowels:", v)
print("Consonants:", c)

'''#output
Enter a string: Hello World
Vowels: 3
Consonants: 7'''