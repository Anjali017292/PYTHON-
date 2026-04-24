# number of rows input by user
rows=int(input("Enter number of rows:"))
if rows>0:
    for i in range(1,rows+1):
        print(" "*(rows-i)+"*"*(i*2-1))
    for i in range(rows-1,0,-1):
        print(" "*(rows-i)+"*"*(i*2-1))
else:
    print("Invalid input")
    
#output:Enter number of rows:5
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
    
    

