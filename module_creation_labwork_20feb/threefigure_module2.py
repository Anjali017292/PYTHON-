from threefigure_module import *

# ---------------- CUBE ----------------
side = float(input("Enter side of cube: "))
print("Cube Volume:", cube_volume(side))
print("Cube Total Surface Area:", cube_total_surface_area(side))

# ---------------- CUBOID ----------------
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Cuboid Volume:", cuboid_volume(l, b, h))
print("Cuboid Total Surface Area:", cuboid_total_surface_area(l, b, h))
print("Cuboid Curved Surface Area:", cuboid_curved_surface_area(l, b, h))

# ---------------- CYLINDER ----------------
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Cylinder Volume:", cylinder_volume(r, h))
print("Cylinder Curved Surface Area:", cylinder_curved_surface_area(r, h))
print("Cylinder Total Surface Area:", cylinder_total_surface_area(r, h))

# ---------------- CONE ----------------
r = float(input("Enter radius of cone: "))
h = float(input("Enter height of cone: "))

print("Cone Volume:", cone_volume(r, h))
print("Cone Curved Surface Area:", cone_curved_surface_area(r, h))
print("Cone Total Surface Area:", cone_total_surface_area(r, h))

# ---------------- SPHERE ----------------
r = float(input("Enter radius of sphere: "))

print("Sphere Volume:", sphere_volume(r))
print("Sphere Surface Area:", sphere_surface_area(r))

# ---------------- HEMISPHERE ----------------
r = float(input("Enter radius of hemisphere: "))

print("Hemisphere Volume:", hemisphere_volume(r))
print("Hemisphere Curved Surface Area:", hemisphere_curved_surface_area(r))
print("Hemisphere Total Surface Area:", hemisphere_total_surface_area(r))