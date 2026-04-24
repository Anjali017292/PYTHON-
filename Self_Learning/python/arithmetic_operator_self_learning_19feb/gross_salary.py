basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
gross = basic + hra + da

print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross)
