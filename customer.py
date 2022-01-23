import itertools

class Customer:

    # transactions can be added later
    def __init__(self, id, name, pnr):
        self.id = id
        self.name = name #str
        self.pnr = pnr #int


c = Customer(1, "Florind", 9905254)
c2 = Customer(2, "adam", 2304021)


print(c)
print(c2)




