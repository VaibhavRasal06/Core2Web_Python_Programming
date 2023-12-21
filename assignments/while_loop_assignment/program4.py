"""WAP to calculate the factorial of a given number.
Input:
5
Output:
Factorial of 5 is 120"""

fact = 1
num = 5
while num >= 1:
    fact *= num
    num -= 1
print("Factorial of 5 is:",fact)
