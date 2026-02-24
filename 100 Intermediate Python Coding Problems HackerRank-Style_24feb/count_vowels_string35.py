#input a string and count the number of vowels in it
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string is {count}")

'''Output:
Enter a string: Hello World
Number of vowels in the string is 3'''