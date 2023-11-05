"""
Program8 :
Row = 3

1 3 5
1 3 5
1 3 5
"""


for i in range(3):
    num = 1
    #num = i + 2
    for j in range(3):
        print(num, end = " ")
        num += 2
    print()
