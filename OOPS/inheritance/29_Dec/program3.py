

class parent:
    
    def __init__(self):
        print("in parent constructor")
        self.x = 10
        self.y = 20

    def dispParent(self):
        print(self.x)
        print(self.y)

class child(parent):
    
    def __init__(self):
        print("in child constructor")
        self.x = 30
        self.y = 40
        super().__init__()

obj = child()
obj.dispParent()
        
