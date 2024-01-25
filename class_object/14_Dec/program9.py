class Ground(object):

    def __init__(self):
        self.Maharashtra = "MCA"
        self.Gujrat = "GCA"
        self.Karnataka = "KCA"

    def state(self):
        print(self.Maharashtra)
        print(self.Gujrat)
        print(self.Karnataka)

obj = Ground()
obj.state()
