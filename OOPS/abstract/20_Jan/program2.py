
from abc import ABC, abstractmethod

class TATA(ABC):

    def slogan(self):
        print("TATA truck is desh ka truck")

    @abstractmethod
    def carType(self):
        pass

class Harrier(TATA):

    def carType(self):
        print("SUV")


class Punch(TATA):

    def carType(self):
        print("Hathpack")

obj1 = Punch()
obj1.carType()

print(Harrier.mro())
print(type(TATA))
print(type(Harrier))




