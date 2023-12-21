"""WAP to print a cube of odd numbers up to n in reverse order.
Input: 15
Output: 3375 2197 1331 729 343 125 27 1"""


num = int(input("Enter a number: "))

print("Cubes of odd numbers up to", num, "in reverse order:")
i = num
while i > 0:
    if i % 2 != 0:
        cube = i ** 3
        print(cube, end=" ")
    i -= 1

