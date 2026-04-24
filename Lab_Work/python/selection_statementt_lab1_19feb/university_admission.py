marks = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
entrance = int(input("Enter entrance exam score: "))

if marks < 75:
    print("Not Eligible: Less than 75% in 12th")
elif maths != "yes":
    print("Not Eligible: Mathematics not studied")
elif entrance < 80:
    print("Not Eligible: Entrance score less than 80")
else:
    print("Eligible for Admission")
