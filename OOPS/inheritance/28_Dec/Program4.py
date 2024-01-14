class parent:

    def __init__(self):
        print("in parent constructor")

    def parentfunc(self):
        print("in parent function")

class child(parent):

    def __init__(self):
        print("in child constructor")

obj1 = child()
obj1.parentfunc()
