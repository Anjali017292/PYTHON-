# Generate multiplication table up to N using while loop
# Input a number N and generate multiplication table up to N
n = int(input("Enter a number: "))
# Initialize multiplier
i = 1
# Generate and print multiplication table up to N
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
    
'''#output:
    Enter a number: 5
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50'''