#WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100

starting = int(input("Enter a starting number: "))
ending = int(input("Enter a ending number: "))

for i in range(starting,ending+1):
    if i % 7 == 0 and i % 3 != 0:
        print(i, end = ' ')
print()
