# Program to search student marks using dictionary
# This program creates a dictionary of student names and their corresponding marks. It then allows the user to search for a student's marks by entering their name. If the student is found in the dictionary, their marks are displayed; otherwise, a message indicating that the student was not found is shown.
students = {
    "Aman": 85,
    "Riya": 90,
    "Karan": 78,
    "Neha": 88
}
# Search for student marks
while True:
    name = input("\nEnter student name to search (or type exit): ")
# The program continues to prompt the user for a student name until they type "exit". If the entered name matches a key in the students dictionary, the corresponding marks are displayed. If the name is not found, a message is printed indicating that the student was not found.
    if name.lower() == "exit":
        break
# The in operator is used to check if the entered name exists as a key in the students dictionary. If it does, the program retrieves and prints the marks associated with that name. If it does not, it prints "Student not found".
    if name in students:
        print(name, "marks =", students[name])
    else:
        print("Student not found")
        
'''#output
Enter student name to search (or type exit): Riya
Riya marks = 90
Enter student name to search (or type exit): Aman
Aman marks = 85
Enter student name to search (or type exit): Neha
Neha marks = 88
Enter student name to search (or type exit): exit
'''