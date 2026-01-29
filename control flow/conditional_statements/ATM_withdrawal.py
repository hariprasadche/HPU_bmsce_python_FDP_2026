#ATM withdrawal
amount = 50000
withdraw = int(input("Enter the amount to withdraw: "))
if withdraw > 50000:
    print("invalid amount")
else:
    if withdraw <= amount:
        print("withdraw", withdraw)
    else:
        print("not withdraw", withdraw)

