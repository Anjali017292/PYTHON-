units = int(input("Enter units consumed: "))
age = int(input("Enter your age: "))

# Calculate bill
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

# Senior citizen discount
if age >= 60:
    bill = bill - (bill * 0.10)

print("Total Electricity Bill =", bill)
