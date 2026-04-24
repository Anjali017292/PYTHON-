amount = float(input("Enter purchase amount: "))

if amount >= 10000:
    discount = 20
elif amount >= 5000:
    discount = 10
else:
    discount = 5

final_amount = amount - (amount * discount / 100)

print("Discount =", discount, "%")
print("Final Amount =", final_amount)
