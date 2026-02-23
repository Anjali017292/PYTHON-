# Input attendance
try:
    attendance = list(map(int, input("Enter attendance (1=Present, 0=Absent): ").split()))
except:
    print("Invalid input")
    exit()

valid_attendance = []

# Validation
for a in attendance:
    if a in [0, 1]:
        valid_attendance.append(a)
    else:
        print("Invalid value removed:", a)

if len(valid_attendance) == 0:
    print("No attendance data available")
    exit()

total_days = len(valid_attendance)
present_days = valid_attendance.count(1)

# Percentage
percentage = (present_days / total_days) * 100
print("Attendance Percentage:", round(percentage, 2))

# Below 75%
if percentage < 75:
    print("Student below 75% attendance")

# Consecutive absences
for i in range(len(valid_attendance) - 1):
    if valid_attendance[i] == 0 and valid_attendance[i+1] == 0:
        print("Warning: Consecutive absences detected")
        
'''output:
Enter attendance (1=Present, 0=Absent): 1 0 1 1 0 0 1
Attendance Percentage: 57.14
Warning: Consecutive absences detected
Enter attendance (1=Present, 0=Absent): 1 1 1 1 1
Attendance Percentage: 100.0    
Enter attendance (1=Present, 0=Absent): 0 0 0 0
Attendance Percentage: 0.0
Warning: Consecutive absences detected
Warning: Consecutive absences detected
'''