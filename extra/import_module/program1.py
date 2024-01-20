
from program2 import *

class BCCI(ICC):

    def __init__(self):
        print("I'm the BCCI")


class IPL(BCCI):

    def __init__(self):
        print("I'm the IPL")

obj = IPL()
