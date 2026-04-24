# Input three sides
side1 = float(input("Enter first side(in cm): "))
side2 = float(input("Enter second side(in cm): "))
side3 = float(input("Enter third side(in cm): "))

# Check Triangle Condition
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Sides must be positive numbers")
elif (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The sides form a Triangle ")
    
    #check type of trinagles
    if side1 == side2 == side3:
        print("It is an Equilateral Triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3 :
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")
else:
    print("The sides do NOT form a Triangle ")