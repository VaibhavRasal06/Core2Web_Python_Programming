"""WAP to find the nth even number.
Input: 3
Output: even number at position 3 is 5"""


n = int(input("Enter the value of n: "))

even_number = 2
count = 1

while count < n:
    even_number += 2
    count += 1

print(f"Even number at position {n} is {even_number}")


