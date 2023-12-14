class employee:

    z = 10

    def __init__(self):
        print("In Constructor")

        self.x = 10
        self.y = 20
    
    def disp (self):
        print(self.x)
        print(self.y)

obj = employee()
obj.disp()
