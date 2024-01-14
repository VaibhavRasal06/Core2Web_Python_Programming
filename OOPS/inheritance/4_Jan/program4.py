
class parent1:

    def __init__(self):
        super().__init__()
        print("In Parent1 Constructor")

    def fun(self):
        print("In fun function")

class parent2:

    def __init__(self):
        super().__init__()
        print("In Parent2 Constructor")

    def data(self):
        print("in data function")

class child(parent2,parent1):
    pass

obj = child()
obj.fun()
obj.data()
