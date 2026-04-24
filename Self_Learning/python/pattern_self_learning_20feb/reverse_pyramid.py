# Reverse Pyramid Pattern
rows = 5
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(1,i+1):
        print(k, end=" ")
    print()

'''output:
 1 2 3 4 5 
  1 2 3 4 
   1 2 3 
    1 2 
     1 '''