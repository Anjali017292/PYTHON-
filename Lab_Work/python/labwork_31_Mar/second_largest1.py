# list of numbers
lst = [10, 20, 4, 45, 99]

# assume first element as largest and second largest
largest = lst[0]
second = lst[0]

# loop through list
for num in lst:
    # if number is greater than largest
    if num > largest:
        second = largest   # update second largest
        largest = num      # update largest
    # check for second largest
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)


'''#output
Second Largest: 45
'''