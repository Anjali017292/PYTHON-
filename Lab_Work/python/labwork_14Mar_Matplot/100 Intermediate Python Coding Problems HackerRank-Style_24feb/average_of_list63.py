#input a list of numbers and calculate the average of all elements in the list
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
count = len(numbers)
#calculate the average and print the list and the average of all elements
average = total_sum / count if count > 0 else 0
print(f"List: {numbers}")
#display the average of all elements in the list
print(f"Average of all elements: {average}")

'''
Output:
List: [1, 2, 3, 4, 5]
Average of all elements: 3.0
'''