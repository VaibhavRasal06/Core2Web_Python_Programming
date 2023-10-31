def facto(a):
    sum = 1
    for i in range(1, a+1):
        sum = sum * i

    return sum

num = int(input("Enter a number: "))
ret = facto(num)
print(ret)

