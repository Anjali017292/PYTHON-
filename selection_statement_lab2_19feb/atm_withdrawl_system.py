balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

if withdraw > balance:
    print("Insufficient Account Balance")
elif withdraw > 50000:
    print("Daily Withdrawal Limit Exceeded")
elif withdraw > atm_cash:
    print("ATM Does Not Have Enough Cash")
else:
    print("Withdrawal Successful")
    print("Remaining Balance =", balance - withdraw)
