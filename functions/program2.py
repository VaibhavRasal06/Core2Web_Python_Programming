def sumNum(x):
    sum = 0
    for i in range(1, x+1):
        sum = sum + i
    print(sum)

val = int(input("Enter a number: "))
sumNum(val)
