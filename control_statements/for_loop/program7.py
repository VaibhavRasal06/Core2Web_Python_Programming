x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

for i in range(x,y+1) :
    if (i % 4 == 0 and i % 5 == 0) :
        print(i)
