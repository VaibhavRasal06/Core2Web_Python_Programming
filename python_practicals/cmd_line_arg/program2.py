import sys

print(sys.argv)

size = len(sys.argv)

add = 0

for i in (1, size):
    add = add + int (sys.argv[i])

print(add)
