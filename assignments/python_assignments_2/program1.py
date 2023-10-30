num = int(input("Enter a number: "))

if (num%4==0 and num%5==0):
    print("{} is divisible by 4 and 5".format(num))
else:
    print("{} is not divisible by 4 and 5".format(num))
