

class Demo:

    def fun(self):
        print("in fun")
    
    def gun(self):
        print("in gun")

obj = Demo()
obj.fun()

obj = None
obj.gun()
