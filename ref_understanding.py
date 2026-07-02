class Customer:
    def __init__(self, name):
        self.name = name


def greet(customer):
    print(id(customer))


    cust = Customer("Ankita")
    print(id(cust))
    greet(cust)