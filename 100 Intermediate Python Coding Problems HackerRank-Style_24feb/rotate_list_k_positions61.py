#input a list of numbers and rotate it k positions to the right
numbers = [1, 2, 3, 4, 5]
k = 2
#rotate the list k positions to the right
rotated_numbers = numbers[-k:] + numbers[:-k]
print(f"Original list: {numbers}")
print(f"Rotated list: {rotated_numbers}")

'''
Output:
Original list: [1, 2, 3, 4, 5]
Rotated list: [4, 5, 1, 2, 3]
'''