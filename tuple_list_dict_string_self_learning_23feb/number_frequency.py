# Program to count frequency of numbers

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Create a dictionary to store frequency of each number
freq = {}
# The get() method of the dictionary is used to retrieve the value for a given key. If the key is not found in the dictionary, it returns a default value (in this case, 0). This allows us to easily count the frequency of each number by incrementing the count for each occurrence of the number in the list.
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
# Display the frequency of each number
print("\nFrequency of each number:")
for key, value in freq.items():
    print(key, ":", value)
    
'''#output
Enter numbers separated by space: 1 2 3 4 2 3
Frequency of each number:
1 : 1
2 : 2
3 : 2
4 : 1'''