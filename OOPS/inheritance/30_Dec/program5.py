

class Demo:

    def __init__(self):
        print("In Constructor")

    def __del__(self):
        print("In Destructor")

    def fun():
        print("In Function")
        obj = Demo()
        print("End Function")
        fun()

obj1 = Demo()
obj2 = Demo()

print("End Code")
