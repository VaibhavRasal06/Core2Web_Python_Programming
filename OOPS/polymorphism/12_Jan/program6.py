

#method overriding

class parent:

    def property(self):
        print("Gold, Car, Benglow")

    def carrer(self):
        print("Eng")

class child(parent):

    def career(self):
        print("Youtuber")

obj1 = child()
obj1.property()
obj1.career()
