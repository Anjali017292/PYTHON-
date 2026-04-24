heart_rate = int(input("Enter heart rate: "))
severe_injury = input("Severe injury? (yes/no): ")
age = int(input("Enter age: "))

if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    condition = "Critical"
elif age > 65:
    condition = "Moderate (Upgraded Priority)"
else:
    condition = "Normal"

print("Patient Condition:", condition)
