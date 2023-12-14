def fun(*argv, a, b):
    print(argv)
    print(a)
    print(b)

fun(1,2,3,3)    #TypeError: fun() missing 2 required keyword-only arguments: 'a' and 'b' 
