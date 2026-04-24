rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = int(input("Enter attendance percentage: "))

if rating >= 4 and experience >= 5 and attendance >= 90:
    increment = 20
elif rating >= 3 and attendance >= 80:
    increment = 10
else:
    increment = 5

print("Increment Percentage =", increment, "%")
