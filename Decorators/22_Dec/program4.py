def normalfun(**args):
    sumData = 0

    for k,v in args.items():
        sumData = sumData + v
    return sumData

print(normalfun(x=10,y=32,z=43))
