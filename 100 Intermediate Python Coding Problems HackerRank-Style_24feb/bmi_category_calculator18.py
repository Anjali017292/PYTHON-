#BMI category calculator
#input weight and height from user
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
#calculate BMI
bmi = weight / (height ** 2)
#check the category of BMI using if-elif-else statements
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
    
#output of the program is shown below:
'''Output:
Enter weight in kg: 70
Enter height in meters: 1.75
Normal weight
Enter weight in kg: 50
Enter height in meters: 1.75
Underweight
Enter weight in kg: 80
Enter height in meters: 1.75
Overweight
Enter weight in kg: 90
Enter height in meters: 1.75
Obese'''