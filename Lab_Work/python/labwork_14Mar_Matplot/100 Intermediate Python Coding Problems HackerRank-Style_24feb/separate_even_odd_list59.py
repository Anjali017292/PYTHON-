#input a list of numbers and separate even and odd numbers from it
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
#using a for loop to iterate through the list and append even numbers to the even_numbers list and odd numbers to the odd_numbers list
for num in numbers:
    #check the current number and its append .
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        #display the current number and its parity
print(f"Original list: {numbers}")
#display the even and odd numbers
print(f"Even numbers: {even_numbers}")
#display the odd numbers
print(f"Odd numbers: {odd_numbers}")

'''
Output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers: [2, 4, 6, 8, 10]
Odd numbers: [1, 3, 5, 7, 9]
'''