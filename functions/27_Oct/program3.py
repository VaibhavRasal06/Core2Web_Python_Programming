def divBy4And5(a):
    for i in range(1,a+1):
        if i%4==0 and i%5==0:
            print(a,"Divisible by 4 & 5")
        else:
            print("Not divisible by 4 and 5")

val = int(input("Enter a number: "))
divBy4And5(val)
