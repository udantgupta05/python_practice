#class Geometry:
#    def area (self, radius):
#        return 3.14 * radius * radius


#    def area(self, l, b):
#        return l*b


#obj = Geometry()
#print(obj.area(4))

#the above code will work in Java

class Geometry:
    def area(self, a, b = 0):
        if b == 0:
            print("Circle", 3.14 * a * a)

        else:
            print("Rect", a * b)


obj = Geometry()
obj.area(4)
obj.area(4, 5)