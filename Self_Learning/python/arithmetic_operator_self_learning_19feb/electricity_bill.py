units = int(input("Enter units consumed: "))
rate = float(input("Enter rate per unit: "))

bill = units * rate
gst = bill * 0.18
total = bill + gst

print("Bill =", bill)
print("GST =", gst)
print("Total Amount =", total)
