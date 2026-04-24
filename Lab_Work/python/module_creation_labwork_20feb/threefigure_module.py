# Value of pi
pi = 3.14

# ---------------- CUBE ----------------
def cube_volume(side):
    return side ** 3

def cube_total_surface_area(side):
    return 6 * side * side


# ---------------- CUBOID ----------------
def cuboid_volume(l, b, h):
    return l * b * h

def cuboid_total_surface_area(l, b, h):
    return 2 * (l*b + b*h + h*l)

def cuboid_curved_surface_area(l, b, h):
    return 2 * h * (l + b)


# ---------------- CYLINDER ----------------
def cylinder_volume(r, h):
    return pi * r * r * h

def cylinder_curved_surface_area(r, h):
    return 2 * pi * r * h

def cylinder_total_surface_area(r, h):
    return 2 * pi * r * (r + h)


# ---------------- CONE ----------------
def cone_volume(r, h):
    return (1/3) * pi * r * r * h

def cone_curved_surface_area(r, h):
    l = (r*r + h*h) ** 0.5
    return pi * r * l

def cone_total_surface_area(r, h):
    l = (r*r + h*h) ** 0.5
    return pi * r * (r + l)


# ---------------- SPHERE -------
def sphere_volume(r):
    return (4/3) * pi * r**3

def sphere_surface_area(r):
    return 4 * pi * r**2


# ---------------- HEMISPHERE ----------------
def hemisphere_volume(r):
    return (2/3) * pi * r**3

def hemisphere_curved_surface_area(r):
    return 2 * pi * r**2

def hemisphere_total_surface_area(r):
    return 3 * pi * r**2