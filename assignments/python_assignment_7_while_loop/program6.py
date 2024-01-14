"""Write a program to count the Odd digits of the given
number.
Input: 942111423
Output: 5"""

number = int(input("Enter a number: "))
count_odd = 0

while number > 0:
 digit = number % 10
 if digit % 2 != 0:
   count_odd += 1
 number //= 10

print(f"The number of odd digits in {number} is {count_odd}")

