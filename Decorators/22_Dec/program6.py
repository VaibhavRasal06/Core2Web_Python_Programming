# decorator chaining

def decorfun(func):
    def wrapper():
        print("start wrapper 2")
        func()
        print("end wrapper 2")
    return wrapper

def decorfun(func):
    def wrapper():
        print("start wrapper 1")
        func()
        print("end wrapper 1")
    return wrapper

@decorfun
@decorfun

def normalfun():
    print("in the normal function")

normalfun()
