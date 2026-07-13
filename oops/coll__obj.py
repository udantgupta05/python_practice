class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def intro(self):
        print("I am", self.name, "and I am", self.age, "old")


c1 = Customer("Nitish", 34)
c2 = Customer("ankit", 45)
c3 = Customer("Neha", 34)

L = [c1,c2,c3]

for i in L:
    i.intro()