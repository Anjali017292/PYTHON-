#input from user
cart = float(input("Enter cart value: "))
member = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is festival season? (yes/no): ")

discount = 0

# Membership discount
if member == "Silver":
    discount = 5
elif member == "Gold":
    discount = 10
elif member == "Platinum":
    discount = 15

# Festival discount
if festival == "yes" and discount < 20:
    discount = 20

final_amount = cart - (cart * discount / 100)

print("Final Payable Amount =", final_amount)
