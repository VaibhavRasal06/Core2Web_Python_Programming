class Human:

    def __init__(self, name, age):
        print("In Demo Constructor")
        self.name = name
        self.age = age

    def information(self):
        print("Name is : ", self.name)
        print("Age is : ", self.age)

name = input("Enter a your name: ")
age = int(input("Enter your age: "))

if __name__ == "__main__":
    obj1 = Human(name, age)
    obj1.information()
