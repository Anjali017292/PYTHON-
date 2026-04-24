#input a list of numbers and check if it is a palindrome
numbers = [1, 2, 3, 2, 1]

#check if the list is a palindrome by comparing it with its reverse
is_palindrome = numbers == numbers[::-1]
#print the list and whether it is a palindrome or not
print(f"List: {numbers}")
print(f"Is palindrome: {is_palindrome}")

'''
Output:
List: [1, 2, 3, 2, 1]
Is palindrome: True
'''