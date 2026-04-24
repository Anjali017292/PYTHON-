amount=float(input("Enter transaction amount:"))
if amount>200000 :
    months=int(input("Account age (in months)"))
    if months<6:
        international=input("Is international?(yes/no)")
        
        if(international=="yes"):
            print("Suspicious transaction flag for verification")
        else:
            print("Not international! Normal transaction")
    else:
        print("Account age is valid normal transaction")
else:
    print("Transaction amount is valid normal transaction")
            
    