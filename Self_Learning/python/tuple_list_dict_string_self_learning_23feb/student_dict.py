# Program to store and display student details using dictionary
# The program prompts the user to enter student details such as name, roll number, course, and marks. It then stores these details in a dictionary and displays them.
student = {}
# Taking input from the user and storing it in the dictionary
student["name"] = input("Enter student name: ")
student["roll"] = int(input("Enter roll number: "))
student["course"] = input("Enter course: ")
student["marks"] = float(input("Enter marks: "))

# Displaying the student details
print("\nStudent Details")
for key, value in student.items():
    print(key, ":", value)
    
'''#output
Enter student name: John Doe
Enter roll number: 123
Enter course: BCA
Enter marks: 85.5
Student Details
name : John Doe
roll : 123
course : BCA
marks : 85.5'''