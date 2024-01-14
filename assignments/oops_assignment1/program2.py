
class Vehicle:

    def __init__(self):
        self.brand = "Tata"
        self.model = "Harrier"
        self.year = 2023
        self.speed = 120

    def accelerate(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)

    def brake(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)

    def honk(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)

class child_vehicle(Vehicle):

    def __init__(self):
        print("in child constructor")

    def accelerate(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)

    def honk(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)
obj = Vehicle()
obj.accelerate()
obj.honk()
obj = child_vehicle()
