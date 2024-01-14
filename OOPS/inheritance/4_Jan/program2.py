# multiple inheritance

class parent1:

    def dispData(self):
        print("In DispData")

class parent2:

    def printData(self):
        print("IN PrintData")

class child(parent2,parent1):
    pass

obj = child()
obj.dispData()
obj.printData()
