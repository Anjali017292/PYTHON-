# Check if a number is an Armstrong number
n = 153
temp = n
sum = 0

# loop until number becomes 0
while temp > 0:
    digit = temp % 10          # get last digit
    sum = sum + digit**3       # cube and add
    temp = temp // 10          # remove last digit

# check result
if sum == n:
    print("True")   # Armstrong number
else:
    print("False")
    
'''# Output:
True
'''