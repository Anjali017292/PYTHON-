#input radius by user
radius= float(input("Enter radius of the circle(in cm)"))

if(radius<=0):
    print("Invalid radius")
    exit()
else:
    #area of circle
    area=3.14*radius*radius
    #perimeter of circle
    perimeter=2*3.14*radius
    print("Area of circle=",area)
    print("perimeter of circle=",perimeter)
