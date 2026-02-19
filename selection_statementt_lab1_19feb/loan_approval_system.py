credit = int(input("Enter credit score: "))
income = float(input("Enter monthly income: "))
existing_loan = float(input("Enter existing loan amount: "))

if credit < 600:
    print("Loan Rejected")
elif credit <= 750:
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected")
    else:
        print("Loan Under Review")
else:
    print("Loan Approved")
