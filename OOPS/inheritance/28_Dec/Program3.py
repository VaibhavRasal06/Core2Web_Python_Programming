
class parent:

    def __init__(self):
        print("in parent constructor")

    def parentfunc(self):
        print("in parant function")

class child(parent):
    pass

obj1 = child()
obj1.parentfunc()
