# This code performs basic arithmetic operations: addition, subtraction, multiplication, and division.
def solve_addition(a, b):
    return a + b

def solve_subtraction(a, b):
    return a - b

def solve_product(a, b):
    return a * b

def solve_division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

print("Addition:", solve_addition(40, 30))
print("Subtraction:", solve_subtraction(50, 40))
print("Product:", solve_product(8, 4))
print("Division:", solve_division(12, 4))


#-----------------------------------------
#'''output:
Addition: 70
Subtraction: 10
Product: 32
Division: 3.0

'''
