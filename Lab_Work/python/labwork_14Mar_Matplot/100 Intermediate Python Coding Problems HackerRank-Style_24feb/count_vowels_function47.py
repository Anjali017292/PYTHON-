#input a string and count the number of vowels in it using a function
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

#call the count_vowels function and print the result
string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"Number of vowels in '{string}': {vowel_count}")

'''
Output:
Enter a string: Hello World
Number of vowels in 'Hello World': 3
'''