student = {}
#to insert an element
student['name'] = 'Aviral'
student['roll'] = 43
student['age'] = 23

print(student)

student["english"] = 89
student["roll"] = 1024

print(student)

for key in student:
    print("key",key,"value",student[key])
    
    
'''#output
{'name': 'Aviral', 'roll': 43, 'age': 23}
{'name': 'Aviral', 'roll': 1024, 'age': 23, 'english': 89}
key name value Aviral
key roll value 1024
key age value 23
key english value 89
'''