# Sort a dictionary by its keys
student_scores = {
    "Charlie": 92,
    "Alice": 95,
    "Bob": 87,
    "Diana": 98,
    "Eve": 89
}
# Sort the dictionary by keys
sorted_dict = dict(sorted(student_scores.items()))
#dict() is used to convert the sorted list of tuples back into a dictionary
print(f"Sorted dictionary: {sorted_dict}")

'''
Output:
Sorted dictionary: {'Alice': 95, 'Bob': 87, 'Charlie': 92, 'Diana': 98, 'Eve': 89}
'''