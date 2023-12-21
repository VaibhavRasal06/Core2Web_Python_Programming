"""WAP to print the first 10 negative numbers which is less than the
given number.
Input:
-5
Output:
first 10 negative numbers less than -5 are
-6 -7 -8 -9 -10 -11 -12 -13 -14 -15"""

num = int(input("Enter a number: "))

print("First 10 negative numbers less than {} are".format(num))
i = num - 1
count = 0
while count < 10:
    print(i, end=" ")
    i -= 1
    count += 1

    

