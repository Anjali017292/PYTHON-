# Sort a dictionary by its values
student_scores = {
    "Charlie": 92,
    "Alice": 95,
    "Bob": 87,
    "Diana": 98,
    "Eve": 89
}
# Sort the dictionary by values in descending order
sorted_dict = dict(sorted(student_scores.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted dictionary by values: {sorted_dict}")

'''
Output:
Sorted dictionary by values: {'Diana': 98, 'Alice': 95, 'Charlie': 92, 'Eve': 89, 'Bob': 87}
'''