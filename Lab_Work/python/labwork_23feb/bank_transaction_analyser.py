# Bank Transaction Analyzer

# Input number of transactions
n = int(input("Enter number of transactions: "))

# Validation
if n <= 0:
    print("Invalid number of transactions")
else:
    transactions = []

    # Input transactions
    for i in range(n):
        t = int(input("Enter transaction (+deposit / -withdrawal): "))
        transactions.append(t)

    # Calculate total balance
    balance = sum(transactions)

    # Find largest withdrawal
    withdrawals = []
    for t in transactions:
        if t < 0:
            withdrawals.append(t)

    if len(withdrawals) > 0:
        largest_withdrawal = min(withdrawals)
    else:
        largest_withdrawal = "No withdrawal"

    # Count deposits greater than 10000
    count = 0
    for t in transactions:
        if t > 10000:
            count += 1

    # Output
    print("Total Balance:", balance)
    print("Largest Withdrawal:", largest_withdrawal)
    print("Deposits greater than 10000:", count)
    
'''#output
Enter number of transactions: 5
Enter transaction (+deposit / -withdrawal): 15000
Enter transaction (+deposit / -withdrawal): -5000
Enter transaction (+deposit / -withdrawal): 25000
Enter transaction (+deposit / -withdrawal): -12000
Enter transaction (+deposit / -withdrawal): 8000
Total Balance: 31000
Largest Withdrawal: -12000
Deposits greater than 10000: 2
'''