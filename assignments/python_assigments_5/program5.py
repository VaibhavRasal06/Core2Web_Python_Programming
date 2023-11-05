"""
Program5 :
Row = 4
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
"""

num = 0
for i in range(4):
    num = 1 + i
    for j in range(4):
        print(num, end = " ")
        num += 1
    print()

