#program to input time in seconds and convert it into hours,minutes and seconds
#input of time in second
second=int(input("Enter time in seconds"))
#____________________________________________
#initialising no. of hours and minutes
minutes=0
hours=0
#calculating hours
if(second>=3600):
    hours=second//3600 #storing quotient as hours
    second=second%3600 #storing remainder as seconds
if(second>=60):
    minutes=second//60
    second=second%60
print("Time in Hours:",hours)
print("Time in Minutes:",minutes)
print("Remaining Seconds:",second)