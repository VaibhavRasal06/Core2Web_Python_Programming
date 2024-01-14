class parent:

    def __init__(self):
        print("in constructor parent")

    def parentfunc(self):
        print("in parent function")

class child(parent):

    def __init__(self):
        #parent()
        #super().__init__()
        parent.__init__(self)
        print("in constructor child")

    def childfunc(self):
        print("in child function")

obj1 = child()
obj1.parentfunc()
obj1.childfunc()

