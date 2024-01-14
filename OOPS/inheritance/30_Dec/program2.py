

def fun():
    print("In Function")

class Demo:

    fun()

    print("Start Class")

    def __init__(self):
        print("In Constructor")

    print("End Class")

print("Start Code")
obj = Demo()
print("End Code")
