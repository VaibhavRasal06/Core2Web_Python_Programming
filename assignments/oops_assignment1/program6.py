
class Owner:

    def __init__(self):
        print("I own the company")

class MD(Owner):

    def __init__(self):
        print("I manage the company")

class CEO(Owner,MD):

    def __init__(self):
        print("I plan and manage the tasks")

class Sen


