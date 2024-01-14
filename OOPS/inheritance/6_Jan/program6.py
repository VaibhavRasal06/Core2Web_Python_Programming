
class GrandParent:
    
    def fun(self):
        print("in parent1 function")

class Parent1(GrandParent):

    def fun(self):
        print("In parent2 function")

class Parent2(GrandParent):

    def fun(self):
        print("In Parent3 Function")

class child(Parent1,Parent2):
    pass

print(child.mro())
