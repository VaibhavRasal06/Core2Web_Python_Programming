
from program4 import *

class Core2Web(Biencaps):

    def __init__(self):
        print("I'm Core2Wb constructor")

class Incubators(Core2Web):

    def __init__(self):
        print("I'm Incubators constructor")
        super().__init__()

if __name__ == '__main__':
    Incubators()
else:
    Core2Web()


