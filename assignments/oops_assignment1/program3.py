
class parent:

    def __init__(self):
        print("In Parent Constructor")
    
    @classmethod
    def clm(self):
        print("in class method")


    @staticmethod
    def stm():
        print("in static method")

obj = parent()
parent.clm()
obj.stm()


