class Phone:
    def __init__(self, price, brand, camera):

        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera


    def buy(self):
        print("Buying a smartphone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")


s = SmartPhone(20000, "Apple", 16)

s.buy()    #method overriding

