class bank_account():
    def __init__(self, account_num: float,):
        self.__account_num = account_num
        self.__balance = 0

    def balance_set (self, balance: float,):
        self.__balance = balance

    def account_num (self, account_num: int,):
        self.__account_num = account_num

    def get_balance (self):
        return self.__balance

    def get_account_num (self):
        return self.__account_num

class Worker:
    def __init__(self, first: str = "", last: str = "", account: str = ""):
        self.first_name = first
        self.last_name = last
        self.account_name = account

class Employee(Worker):
    def __init__(self, in_salary: float, first: str = "", last: str = "", account: str = "" ):

        super().__init__(first, last, account,)
        self.salary = in_salary

class Contractor(Worker):
    def __init__(self, rate_per_hour: float, first: str = "", last: str = "", account: str = ""  ):

        super().__init__(first, last, account,)
        self.rate = rate_per_hour


c = Contractor(60.00, "Bob", "Dylan", "bdylan")
e = Employee(600, "jim", "hendrix", "jhendrix")

print(c.first_name + " " + c.last_name + " has hourly wages of " + str(c.rate))
print(e.first_name + " " + e.last_name + " has weekly wages of " + str(e.salary))