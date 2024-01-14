def func(num):

    def digitCount(num):

        return len(str(num))

    def evendigitCount(num):

        return sum(1 for digit in str(num) if int(digit) % 2 == 0)

    def odddigitCount(num):

        return sum(1 for digit in str(num) if int(digit) % 2 != 0)

    return [digitCount(num),evendigitCount(num),odddigitCount(num)]

num = int(input("Enter a number: "))

result = func(num)
print(result)
