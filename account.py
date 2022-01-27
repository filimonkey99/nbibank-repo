

class Account:


    def __init__(self, account_nr:int):
        self.balance = 0
        self.account_type = "debit acocunt"
        self.account_nr = account_nr

    def get_account_info(self):
        return f" your {self.account_type} has {self.balance} $ and your account number is {self.account_nr}"

    def withdraw(self, money:float):
        if money <= self.balance:
            self.balance -= money
            print(f"You have succesfully withdrawn {money} $, your current balance is {self.balance} $")
        else:
            print(f"Your account dose not have enough money, your current balance is {self.balance} $, to increase balance make a deposit")

    def deposit(self, money:float):
        self.balance += money
        print(f"You have deposited {money} and your balance is now {self.balance}")
        return self.balance






