#input a list of numbers and count the frequency of each element in it
numbers = [1, 2, 3, 2, 4, 1, 5]
frequency = {}
#print(f"Initial frequency dictionary: {frequency}")
for num in numbers:
    #check if the number is already in the frequency dictionary
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
        #display the current number and its frequency
print(f"Original list: {numbers}")
print(f"Frequency count: {frequency}")

'''
Output:
Original list: [1, 2, 3, 2, 4, 1, 5]
Frequency count: {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}
'''