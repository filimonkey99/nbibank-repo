import customer
import account
class Bank:
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
        print()

    def add_customers(self, fname, lname, pnr):
        """Skapar en ny kund med namn och personnummer. Kunden skapas endast om det inte
        finns någon kund med personnumret som angetts. Returnerar True om kunden skapades
        annars returneras False."""
        self.fname = fname
        self.lname = lname
        self.pnr = pnr

        prospect = customer.Customer(fname , lname, pnr)
        duplicate_pnr =False
        if self.customers == []:
            self.customers.append(prospect)
            print(f"Welcome to Filibank {prospect.fname} \n Here is your customer info, \n Name; {fname} {lname} Social security number: {pnr}")
        else:
            for p in self.customers:
                if p.pnr != prospect.pnr:
                    self.customers.append(prospect)
                    print(f"Welcome to Filibank {prospect.fname} \n Here is your customer info, \n Name; {fname} {lname} Social security number: {pnr}")
                else:
                    duplicate_pnr =True
                    return f"This social security number already exists, are you trying to commmit fraud {fname}?"




    def get_customer_with_pnr(self, pnr):
        for i in self.customers:
            if i.pnr == pnr:
                print(f",Customer found! Name:{i.fname} {i.lname} social security number:{i.pnr}")
            else:
                print("customer does not yet exist or you erote the wrong social security number")

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

    def add_account(self, pnr):
       """ Skapar ett konto till kunden med personnumret som angetts, returnerar kontonumret som det skapade
        kontot fick alternativt returneras –1 om inget konto skapades."""

    def get_account(self, pnr, account_id):
        """returnerar textuell info av kontot med konto nummer som tillhör kunden (kontonummer, saldo och kontotyp)"""

    def deposit(self, pnr, account_id, amount):
        """gör insättning på kontot returnerar true om det gick annars false"""

    def withdraw(self, pnr, account_id, amount):
        """gör uttag på kontot returnerar true om det gick bra annars false"""

    def close_account(self, pnr, account_id):
        """avslutar konto, textuell info presenteras av konto o saldo genereras och returneras"""