# Number Pyramid Pattern
rows = 5
for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    print()
    
'''output:
        1 
      1 2 
    1 2 3 
  1 2 3 4   
1 2 3 4 5
'''