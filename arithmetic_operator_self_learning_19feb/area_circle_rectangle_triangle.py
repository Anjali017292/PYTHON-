radius = float(input("Enter radius: "))
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
base = float(input("Enter base: "))
height = float(input("Enter height: "))

circle = 3.14 * radius ** 2
rectangle = length * breadth
triangle = (base * height) / 2

print("Area of Circle =", circle)
print("Area of Rectangle =", rectangle)
print("Area of Triangle =", triangle)
