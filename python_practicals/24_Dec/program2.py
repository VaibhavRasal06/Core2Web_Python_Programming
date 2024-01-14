"""Write a program to check whether the number is a Prime
number or not. (2332)
Input:2332
Output:2332 is not a prime number"""

val = int(input("Enter a number: "))
i = 2

while (i <= val // 2):
    if val % i == 0:
        print(val,"is not a prime number")
        break
    i += 1
else:
    print(val, "is prime number")
