import customer
import account
class Bank:
    all_accounts= []
    all_customers = []

    def __init__(self):
        self.bank_name = "FiliBank"
        self.customers = []

    def get_customers(self):
        #Returnerar bankens alla kunder (personnummer och namn)
        all_customers=[]
        for customer in self.customers:
            customer_info= customer.pnr, customer.fname, customer.lname, customer.id
            all_customers.append(customer_info)
        return all_customers


    def _load(self):
        #Läser in text filen och befolkar listan som ska innehålla kunderna.
        for line in open("Customer_database.txt").readlines():
            consumer = line.strip().split(':')

            for x in self.customers:

                if consumer[3] != x.pnr:

                    if int(consumer[0]) != int(x.id):
                        client = customer.Customer(consumer[1], consumer[2], consumer[3], consumer[0])
                        self.customers.append(client)
                        break
                    else:
                        client = customer.Customer(consumer[1], consumer[2], consumer[3])
                        self.customers.append(client)
                        break
                else:
                    print( "They are already our client.")
                    break
        return self.customers

    def add_customers(self, fname, lname, pnr):
        """Skapar en ny kund med namn och personnummer. Kunden skapas endast om det inte
        finns någon kund med personnumret som angetts. Returnerar True om kunden skapades
        annars returneras False."""
        self.fname = fname
        self.lname = lname
        self.pnr = pnr

        prospect = customer.Customer(fname, lname, pnr)
        duplicate_pnr =False
        if self.customers == []:
            self.customers.append(prospect)
            print(f"Welcome to Filibank {prospect.fname} \n Here is your customer info, \n Name: {fname} {lname} Social security number: {pnr}")
        else:
            for p in self.customers:
                if p.pnr != prospect.pnr:
                    self.customers.append(prospect)
                    print(f"Welcome to Filibank {prospect.fname} \n Here is your customer info, \n Name; {fname} {lname} Social security number: {pnr}")
                else:
                    duplicate_pnr =True
                    return f"This social security number already exists, are you trying to commmit fraud {fname}?"
        return duplicate_pnr


    def get_customer_with_pnr(self, pnr):
        for i in self.customers:
            if i.pnr == pnr:
                print(f",Customer found! Name:{i.fname} {i.lname} social security number:{i.pnr}")
            else:
                print("customer does not yet exist or you wrote the wrong social security number")

    def change_customer_name(self, fname, lname, pnr):
        #Byter namn på kund, returnerar True om namnet ändrades annars returnerar det False (om kunden inte fanns).
        for n in self.customers:
            if n.pnr == pnr:
                n.fname = fname
                n.lname = lname
                print(f"Congratulations on your new name {fname} {lname} !!")
            else:
                return False

    def remove_customer(self, pnr):
       """ Tar bort kund med personnumret som angetts ur banken, alla kundens eventuella konton tas också bort och
        resultatet returneras. Listan som returneras ska innehålla information om alla konton sotogs bort, saldot som kunden får tillbaka.
        """
       return_balance = 0
       customer = []
       all_accounts = []
       for x in self.customers:
           if x.pnr == pnr:
               customer = self.customers.index(x)
               self.customers.pop(customer)

               for y in x.accounts:
                   return_balance = y.balance
               return f"Customer {x.fname} {x.lname} is deleted\n" \
                      f"Return balance: {return_balance}"
           else:
               f"Customer with personal number: {pnr} not found!"

    def add_account(self, pnr):
       """ Skapar ett konto till kunden med personnumret som angetts, returnerar kontonumret som det skapade
        kontot fick alternativt returneras –1 om inget konto skapades."""

       temp = []
       for x in self.all_customers:
           if x.pnr == pnr:
               for y in self.all_accounts:
                   if y.customer_id == x.id:
                       temp.append(y)

    def get_account(self, pnr, account_nr):
        """returnerar textuell info av kontot med konto nummer som tillhör kunden (kontonummer, saldo och kontotyp)"""
        for x in self.all_customers:
            if x.ssn == pnr:
                for y in self.all_accounts:
                    if y.account_nr == account_nr:
                        return y

    def deposit(self, pnr, account_nr, money):
        """gör insättning på kontot returnerar true om det gick annars false"""

        empty_list = []
        for x in self.all_customers:
            if x.pnr == pnr:
                for z in self.all_accounts:
                    if z.account_nr == account_nr:
                        empty_list.append(z)
                        for y in empty_list:
                            if z.account_nr == account_nr:
                                z.balance += money
                                return True
                            else:
                                return False



    def withdraw(self, pnr, account_nr, money):
        """gör uttag på kontot returnerar true om det gick bra annars false"""
        for x in self.all_customers:
            if x.pnr == pnr:
                for y in self.all_accounts:
                    if y.account_nr == account_nr:
                        if y.balance >= money:
                            y.balance -= money
                            return True
                        else:
                            return False


    def close_account(self, pnr, account_nr):
        """avslutar konto, textuell info presenteras av konto o saldo genereras och returneras"""

        for x in self.customers:
            if x.pnr == pnr:
                for y in x.accounts:
                    if y.account_nr == account_nr:
                        x.close_account(account_nr)
                        return f"Account {account_nr} has been closed, you will be reimbursed {y.balance}$"
                    else:
                        return f"Account {account_nr} is not in our system"
            else:
                return f"Customer with the social security number {pnr} does not exist in our database."