# Find the top scorer in a dictionary of student scores
student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 98,
    "Eve": 89
}
# Find the student with the highest score
topper = max(student_scores, key=student_scores.get)
print(f"Top scorer: {topper} with score {student_scores[topper]}")

'''
Output:
Top scorer: Diana with score 98
'''