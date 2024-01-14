"""Write a program to count the even digits of the given
number.
Input: 942111423
Output: 4"""

number = int(input("Enter a number: "))
count_even = 0

while number > 0:
 digit = number % 10
 if digit % 2 == 0:
   count_even += 1
 number //= 10

print(f"The number of even digits in {number} is {count_even}")

