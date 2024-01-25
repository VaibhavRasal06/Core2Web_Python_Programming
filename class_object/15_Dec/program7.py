
class Captain:

    def __init__(self, captain_name, age):
        self. captain_name = captain_name
        self.age = age

    def captain_info(self):
        print(self.captain_name)
        print(self.age)

IND = Captain("Rohit Sharma", 35)
END = Captain("Ben Stokes", 34)
NZE = Captain("Ken Villamance",33)
AUS = Captain("Pat Cammunis", 32)

IND.captain_info()
END.captain_info()
NZE.captain_info()
AUS.captain_info()
