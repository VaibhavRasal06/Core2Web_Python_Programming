def fun(x,y,**argv):
    print(type(argv))
    print(x)
    print(y)
    print(argv)

fun(x=10,y=20,z=12)
