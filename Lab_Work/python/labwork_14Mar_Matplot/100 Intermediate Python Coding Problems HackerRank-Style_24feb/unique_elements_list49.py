#input a list of numbers and print the unique elements in it using a function
def unique_elements(numbers_list):
    unique_list = []
    for num in numbers_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

#call the unique_elements function and print the result
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(x) for x in numbers]
unique_numbers = unique_elements(numbers)
print(f"Unique elements in the list: {unique_numbers}")

'''
Output:
Enter a list of numbers separated by spaces: 1 2 3 2 4 1 5
Unique elements in the list: [1, 2, 3, 4, 5]
'''