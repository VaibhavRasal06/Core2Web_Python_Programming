
class Demo:

    def __init__(self):

        print("In Constructor")

    def __del__(self):
        print("In Destructor")

obj1 = Demo()
obj2 = Demo()


