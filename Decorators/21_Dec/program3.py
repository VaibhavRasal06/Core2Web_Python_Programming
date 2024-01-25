
#class College(fun):

def college(fun):

    def HOD():
        print("Hello World")
        fun()
        print("Hello College")

    return HOD

def teachers():
    print("Hello MH")

obj = college(teachers)
obj()
