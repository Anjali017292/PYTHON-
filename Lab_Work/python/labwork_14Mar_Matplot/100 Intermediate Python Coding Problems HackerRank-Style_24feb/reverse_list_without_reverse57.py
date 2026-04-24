#input a list of numbers and reverse it without using the reverse() function
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
#using a for loop to iterate through the list in reverse order and append each element to the reversed_numbers list
for i in range(len(numbers) - 1, -1, -1):
    #in append the current element to the reversed_numbers list
    reversed_numbers.append(numbers[i])
print(f"Original list: {numbers}")
#display the reversed list
print(f"Reversed list: {reversed_numbers}")

'''
Output:
Original list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
'''