#WAP to prints numbers which are divisible by 3 and 5 both in a given range.
start = int(input("Enter a start value: "))
end = int(input("Enter a end value: "))

for i in range(start,end+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end = ' ')

print()
