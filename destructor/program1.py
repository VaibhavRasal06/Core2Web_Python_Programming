
class Company:

    def Manager(self):
        print("Hello")

    def developer(self):
        print("Okay")

    def __del__(self):
        print("Done")

obj = Company()
obj.Manager()
#obj.developer()

del obj
#obj.developer()

