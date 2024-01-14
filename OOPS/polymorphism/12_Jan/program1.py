class Demo:

    def fun(self):
        print("In Demo fun")

class Memo:


    def fun(self):
        print("In Memo fun")

def callfun(obj):
    obj.fun()

obj1 = Demo()
obj2 = Memo()

callfun(obj2)
