#input a list of numbers and replace all negative numbers with 0
numbers = [1, -2, 3, -4, 5]
#replace all negative numbers with 0
numbers = [num if num >= 0 else 0 for num in numbers]
#print the original list and the modified list with negative numbers replaced by 0
print(f"Original list: {numbers}")

'''
Output:
Original list: [1, 0, 3, 0, 5]
'''