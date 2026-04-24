# Pallidrome Number Pattern
rows = 5
for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
        
    for j in range(i,0,-1):
        print(j, end=" ")
        
    for j in range(2,i+1):
        print(j, end=" ")
        
    print()
    
    
'''output:
        1 
      2 1 2 
    3 2 1 2 3 
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''