
class parent:

    def __init__(self):
        print("In Parent Constructor")

    def fun(self):
        print("In parent function")

class child(parent):

    def __init__(self):
        super().__init__()
        print("In child constructor")

    def data(self):
        print("In child data")

obj = child()
obj.fun()
obj.data()
