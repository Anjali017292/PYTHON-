#input a list of numbers and find the second largest element in it
numbers = [10, 25, 3, 45, 5, 89, 2]
largest = numbers[0]
second_largest = numbers[0]
#print(f"Initial largest: {largest}, Initial second largest: {second_largest}")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
        #check if the new largest is greater than the second largest
    elif num > second_largest and num != largest:
        second_largest = num
        
        #display the current number, largest and second largest
print(f"The second largest element in the list is: {second_largest}")

'''
Output:
The second largest element in the list is: 25
'''