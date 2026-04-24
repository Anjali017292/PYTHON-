# Program to find largest and smallest number in a list
# The program prompts the user to enter a list of numbers, then uses the built-in max() and min() functions to find and display the largest and smallest numbers in the list.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find the largest and smallest numbers in the list
largest = max(numbers)
smallest = min(numbers)

# Display the results
print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)


'''output:Enter numbers separated by space: 5 9 2 14 7
List: [5, 9, 2, 14, 7]
Largest number: 14
Smallest number: 2
Enter numbers separated by space: -3 0 8 1 -5
List: [-3, 0, 8, 1, -5]
Largest number: 8
Smallest number: -5'''