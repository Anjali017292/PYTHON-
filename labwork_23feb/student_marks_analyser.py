# to take input from user
try:
    marks = list(map(int, input("Enter marks: ").split()))
except:
    print("Invalid input")
    exit()

valid_marks = []

# Remove invalid marks from list
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)
    else:
        print("Invalid mark removed:", m)

if not valid_marks:
    print("No valid marks available")
else:
    avg = sum(valid_marks) / len(valid_marks)

    # Find toppers in the class
    highest = max(valid_marks)
    toppers = [m for m in valid_marks if m == highest]

    # grade calculation
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Valid Marks:", valid_marks)
    print("Average:", round(avg,2))
    print("Topper Marks:", toppers)
    print("Grade:", grade)
    
    '''output:
    Enter marks: 85 92 78 105 -5 88
    Invalid mark removed: 105
    Invalid mark removed: -5
    Valid Marks: [85, 92, 78, 88]
    Average: 85.25
    Topper Marks: [92]
    Grade: B'''