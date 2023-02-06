class ATM:
    def __init__(self):
        self.balance = 50000

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print(f"Deposited Amount: {deposit_amt}\nUpdated Balance: {self.balance}")

    def withdraw(self, with_amt):
        self.balance -= with_amt
        print(f"Withdrawn Amount: {with_amt}\nUpdated Balance: {self.balance}")


a1 = ATM()
print(f"Balance: {a1.balance}")
dep_amt = int(input("Enter the amount to be deposited: "))
a1.deposit(dep_amt)
withdraw_amt = int(input("Enter the amount to be withdrawn: "))
a1.withdraw(withdraw_amt)
