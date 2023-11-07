n = 6
for i in range(n-1):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i):
        print("R", end = " ")
    for j in range(i+1):
        print("A", end = " ")

    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i,n-1):
        print("S", end = " ")
    for j in range(i,n):
        print("A", end = " ")
    print()
