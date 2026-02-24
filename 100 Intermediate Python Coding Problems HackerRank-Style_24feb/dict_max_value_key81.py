# Find the key with the maximum value in a dictionary
student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 98,
    "Eve": 89
}
# Find the key with the maximum value
max_key = max(student_scores, key=student_scores.get)
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {student_scores[max_key]}")

'''
Output:
Key with maximum value: Diana
Maximum value: 98
'''