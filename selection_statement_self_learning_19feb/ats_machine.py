balance = 50000
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient Balance")
elif withdraw > 20000:
    print("Limit Exceeded")
else:
    print("Withdrawal Successful")
    print("Remaining Balance =", balance - withdraw)
