x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

for i in range(x,y+1):
    if i%2 == 0 or i%3==0:
        print(i)
