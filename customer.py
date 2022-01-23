import account

class Customer:

    # transactions can be added later
    #fname stands for first name and lname stands for last name
    def __init__(self, id:int, fname:str, lname:str, pnr:int):
        self.id = id
        self.fname = fname #str
        self.lname = lname #str
        self.pnr = pnr #int

    def show_customer(self):
        return f"Here's our loyal customer of filibank {self.fname} {self.lname} with social security number {self.pnr} has the customer id of {self.id}"

    def change_firstname(self,fname):
        self.fname = fname
        print(f"Your new first name is {self.fname}")

    def change_firstname(self, fname):
        self.fname = fname
        print(f"Your new first name is now {self.fname}")

    def change_lastname(self, lname):
        self.lname = lname
        print(f"Your new last name is {self.lname}")




c = Customer(1, "Florind","Haliti", 9905254)
a = Customer(2, "adam","Johansson", 2304021)


print(c.show_customer())
print(a.show_customer())




