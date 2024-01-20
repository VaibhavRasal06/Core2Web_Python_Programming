

from abc import ABC, abstractmethod

class Primeur_Leauge(ABC):

    def rule(self):
        print("Leauges rule are different")

    @abstractmethod
    def overs(self):
        print("Overs are different at different leagues")

obj = Primeur_Leauge()
