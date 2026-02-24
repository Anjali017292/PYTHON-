#input username and password from user
username = input("Enter username: ")
password = input("Enter password: ")
#check whether the username and password are valid using if-elif-else statements
if username == "admin" and password == "password123":
    print("Login successful!")
elif username == "admin":
    print("Incorrect password.")
elif password == "password123":
    print("Incorrect username.")
else:
    print("Invalid username and password.")
    
#output of the program is shown below:
'''Output:
Enter username: admin
Enter password: password123
Login successful!
Enter username: admin
Enter password: wrongpassword
Incorrect password.
Enter username: wrongusername
Enter password: password123
Incorrect username.
Enter username: wrongusername
Enter password: wrongpassword
Invalid username and password.'''