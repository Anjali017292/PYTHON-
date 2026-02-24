# Safely remove a key from a dictionary
student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 98,
    "Eve": 89
}
key_to_remove = "Charlie"
# Check if the key exists before removing it
if key_to_remove in student_scores:
    del student_scores[key_to_remove]
print(f"Dictionary after removing '{key_to_remove}': {student_scores}")

'''
Output:
Dictionary after removing 'Charlie': {'Alice': 95, 'Bob': 87, 'Diana': 98, 'Eve': 89}
'''