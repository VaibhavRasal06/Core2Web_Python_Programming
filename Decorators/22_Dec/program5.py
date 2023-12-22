def decorfun(func):
    print("in decor function")

    def wrapper(*args):
        print("start the wrapper")
        val = func(*args)
        print("End the wrapper")
        return val
    return wrapper

@decorfun
def normalfun(x,y):
    print("in the normal function")
    return x + y

print(normalfun(10,20))


