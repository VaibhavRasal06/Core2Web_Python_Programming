x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print("--------------------------------")

for i in range(x, y+1):
    if (i % 2 == 0):
        print("{} is even number".format(i))
    else:
        print("{} is odd number".format(i))
