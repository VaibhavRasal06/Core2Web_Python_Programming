"""
Program2 :
Rows = 4

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""

rows = int(input("Enter a number of rows: "))

num = 1

for i in range(rows):
    for j in range(rows):
        print(num, end = " \t")
        num += 1
    print()
