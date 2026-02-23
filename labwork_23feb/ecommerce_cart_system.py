# Take input
try:
    prices = list(map(int, input("Enter product prices: ").split()))
except:
    print("Invalid input")
    exit()

# Remove duplicate products
unique_prices = []
for p in prices:
    if p not in unique_prices:
        unique_prices.append(p)

# Calculate subtotal
total = sum(unique_prices)
print("Subtotal:", total)

# Discount
discount = 0
if total > 5000:
    discount = total * 0.10
    print("Discount Applied:", discount)

total_after_discount = total - discount

# GST
gst = total_after_discount * 0.18

# Final amount
final_amount = total_after_discount + gst

print("GST:", gst)
print("Final Payable Amount:", round(final_amount, 2))


'''output:
Enter product prices: 1000 2000 3000 1000
Subtotal: 7000
Discount Applied: 700.0
GST: 1134.0
Final Payable Amount: 8434.0
Enter product prices: 500 1500 2500 500
Subtotal: 5000
GST: 900.0
Final Payable Amount: 5900.0
'''