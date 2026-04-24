# Reverse a string using a for loop
input_string = input("Enter a string: ")
reversed_string = ""
# The variable reversed_string is initialized as an empty string. This variable will be used to build the reversed version of the input string as we iterate through it.
for char in input_string:
    reversed_string = char + reversed_string
    # This line adds the current character to the front of the reversed_string, effectively reversing it as we iterate through the input_string.
print("Reversed string:", reversed_string)


'''Output:  
Enter a string: Hello, World!
Reversed string: !dlroW ,olleH'''