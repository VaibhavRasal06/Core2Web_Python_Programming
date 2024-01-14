"""4. Write a program to count the digits of the given number.
Input:942111423
Output: 9"""

number = int(input("Enter a number: "))
count = 0
while number > 0:
  count += 1
  number //= 10

print(f"The number of digits in {number} is {count}")

