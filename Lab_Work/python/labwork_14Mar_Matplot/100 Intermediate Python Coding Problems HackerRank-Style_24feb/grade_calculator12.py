#input from user to check the grade
marks = int(input("Enter your marks: "))
#check the grade using if-elif-else statements
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    
'''Output:
Enter your marks: 85
Grade: B
Enter your marks: 72
Grade: C'''