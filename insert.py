# Program to calculate Simple Interest

# Input from user
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest =", round(simple_interest,2))
