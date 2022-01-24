import customer
import account
class Bank:
    def __init__(self):
        self.bank_name = "Filibank"
        self.customers = []

    def get_customers(self):
        #Returnerar bankens alla kunder (personnummer och namn)
        for customer in self.customers:
            print(customer)

    def _load(self):
        #Läser in text filen och befolkar listan som ska innehålla kunderna.
        print()

    def add_customers(self, name, pnr):
        """Skapar en ny kund med namn och personnummer. Kunden skapas endast om det inte
        finns någon kund med personnumret som angetts. Returnerar True om kunden skapades
        annars returneras False."""
        self.name = name
        self.pnr = pnr


    def get_customer(self,name, pnr):
        self.pnr = pnr

    def change_customer_name(self, name, pnr):
        #Byter namn på kund, returnerar True om namnet ändrades annars returnerar det False (om kunden inte fanns).
        self.name = name
        self.pnr = pnr

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