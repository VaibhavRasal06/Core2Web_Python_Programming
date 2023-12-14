def addByten(x,y,z):
    x = x + 10
    y = y + 10
    z = z + 10
    return x, y, z

val_1 = int(input("Enter a value of 1: "))
val_2 = int(input("Enter a value of 2: "))
val_3 = int(input("Enter a value of 3: "))

retval = addByten(val_1, val_2, val_3)
print(type(retval))
for i in retval:
    print(i)

a, b, c = addByten(val_1, val_2, val_3)


"""print(a)
print(b)
print(c)"""
