# Check if a key exists in a dictionary
student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 98,
    "Eve": 89
}
key_to_check = "Charlie"
if key_to_check in student_scores:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")

'''
Output:
Key 'Charlie' exists in the dictionary.
'''