class account:

    __amount = 0


    def __init__(self, initial_amount = 0):
        self,__balance = initial_amount

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount

    def withdraw(self, withdraw_amount):
        self.__balance += withdraw_amount

    def withdraw(self):
        return self.__balance

new_account = account(123456)

#print(new_book.isbn)

new_account.set_balance(23456)

print(new_account.get_balance())

