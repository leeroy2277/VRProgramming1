class BankAccount:
    Balance = ""

    def __init__(self, input_deposit):
        self.Balance = input_deposit

    def __init__(self, input_withdraw):
        self.Balance = input_withdraw

    def declare_yourself(self):
        print("balance is " + self.Balance)

b = BankAccount(10)
b.deposit(25)
b.withdraw(1)
print("the balance of th bank account is now " + str(b.balance))


