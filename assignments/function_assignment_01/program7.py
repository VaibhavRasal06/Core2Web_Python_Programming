class Sum:

    def mySum(self,num1,num2):
        return num1 + num2

    obj1 = Sum()
    obj2 = Sum()

    obj1_num1 = int(input("Enter a number: "))
    obj2_num2 = int(input("Enter a number: "))

    obj2_num1 = int(input("Enter a number: "))
    obj2_num2 = int(input("Enter a number: "))

    sum1 = obj1.mySum(obj1_num1, obj1_num2)
    sum2 = obj2.mySum(obj2_num2, obj2_num2)

    total_sum = sum1 + sum2

    if total_sum % 2 == 0:
        print("Sum is Even", total_sum)

    else:
        print("Sum is odd", total_sum)
