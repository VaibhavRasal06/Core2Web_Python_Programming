# Decorator in python

"""there are two types of decorators
first is class decorators and second is function decorators"""

def decorfun(func):

    def wrapper():
        print("Start Wrapper")
        func()
        print("End Wrapper")

    return wrapper

@decorfun
def normalfun():
    print("Hello in Normal fun")

normalfun()
