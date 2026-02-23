# Enter number of students
n = int(input("Enter number of students: "))

if n < 3:
    print("Not enough students")
else:
    scores = []

    # Input scores
    for i in range(n):
        s = int(input("Enter score: "))
        scores.append(s)

    # Remove lowest two scores
    scores.sort()
    scores = scores[2:]

    # Add grace marks
    for i in range(len(scores)):
        if 30 <= scores[i] <= 35:
            scores[i] += 5

    # Count passed students
    passed = 0
    for s in scores:
        if s >= 40:
            passed += 1

    print("Updated Scores:", scores)
    print("Number of students passed:", passed)
    
'''#output
Enter number of students: 5
Enter score: 25
Enter score: 30
Enter score: 35
Enter score: 40
Enter score: 45
Updated Scores: [35, 40, 45]
Number of students passed: 3
'''