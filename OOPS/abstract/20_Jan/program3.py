

from abc import ABC, abstractmethod

class RBI(ABC):

    def currenecy(self):
        print("RBI currency is Rupees")

    @abstractmethod
    def loanPer(self):
        print("RBI's 1 ruppes values is equal to 0.82")

class HDFC(RBI):

    def loanPer(self):
        return "HDFC's Loan percentage is 14%"


class Bank_Of_Badoda(RBI):

    def loanPer(self):
        print ("Bank_Of_Badoda's Loan percentage is 12%")


class BankOfMaharashtra(RBI):

    def loanPer(self):
        print("Bank Of Maharashtra Loan percentage is 10%")

obj1 = HDFC()
print(obj1.loanPer())

print(HDFC.mro())
