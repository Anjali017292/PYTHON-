# Right Aligned Triangle Pattern
rows = 5
for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
    
'''output:
        *
        * *
        * * *
        * * * *
        * * * * *
'''