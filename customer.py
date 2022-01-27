import account
import itertools

class Customer:
    id =itertools.count()

    # transactions can be added later
    #fname stands for first name and lname stands for last name
    def __init__(self, fname:str, lname:str, pnr:str , id:int = None ):
        self.fname = fname #str
        self.lname = lname #str
        self.pnr = pnr #str
        self.accounts = []
        if id:
            self.id = id
        else:
            self.id = next(self.id)
            self.id = 1000 + self.id

    def show_customer(self):
        return f"Here's our loyal customer of Filibank {self.fname} {self.lname} with social security number {self.pnr} has the customer id of {self.id}"


    def change_firstname(self,fname):
        self.fname = fname
        print(f"Your new first name is {self.fname}")

    def change_lastname(self, lname):
        self.lname = lname
        print(f"Your new last name is {self.lname}")

    def change_customer_name(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def add_account(self):
        ac = account.Account()
        self.accounts.append(ac)
        print(f"Account created! \n Account {ac.account_nr} is a {ac.account_type} and has currently a balance of {ac.balance}")

    def close_account(self, account_nr):
        for x in self.accounts:
            if account_nr == x.account_nr:
                account = self.accounts.index(x)
                self.accounts.pop(account)
                break




