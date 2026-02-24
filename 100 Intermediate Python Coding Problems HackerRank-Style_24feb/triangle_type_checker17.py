#input three sides of triangle
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
#check the type of triangle using if-elif-else statements
#check whether the triangle is equilateral using if statement
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
    #check whether the triangle is isosceles or scalene using elif statement
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")
    
    
#output of the program is shown below:
'''Output:
Enter first side: 5
Enter second side: 5
Enter third side: 5
The triangle is an equilateral triangle.'''