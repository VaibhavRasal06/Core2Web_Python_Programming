class Parent:

    def __init__(self):
        print("In Parent constructor")

    def parent_fun(self):
        print("in parent fun")

class Child(Parent):

    def __init__(self):
        print("in Child constructor")

    def child_fun(self):
        print("in child fun")

obj = Child()
obj.child_fun()
