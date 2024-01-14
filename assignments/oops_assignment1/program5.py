
class ICC:

    def __init__(self):
        print("I'm the International cricket board")

    def ICC_fun(self):
        print("I control all cricket boards")

class BCCI(ICC):

    def __init__(self):
        print("Im the Indian Cricket Board")

    def BCCI_fun(self):
        print("I control whole India country statewise boards")

class IPL(BCCI):

    def __init__(self):
        print("I'm the Indian Primier League")

    def IPL_fun(self):
        print("I arrange the IPL in India")

obj = IPL()
obj.ICC_fun()
obj.BCCI_fun()
obj.IPL_fun()
