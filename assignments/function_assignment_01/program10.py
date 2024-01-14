'''10. Write a program in which you have to write a __new__ user-defined function that
creates a new instance of a class.'''

class User:
    def __new__(cls):
        instance = super(User, cls).__new__(cls)
        print("Inside User constructor")
        return instance

    def fun(self):
        print("Hello in User function")

obj = User()
obj.fun()

