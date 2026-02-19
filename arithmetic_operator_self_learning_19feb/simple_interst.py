p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100
ci = p * (1 + r/100) ** t - p

print("Simple Interest =", si)
print("Compound Interest =", ci)
