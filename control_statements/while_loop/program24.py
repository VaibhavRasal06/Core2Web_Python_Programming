"""WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100
Input :Enter start of range - 1
Enter end of range - 100
Output : 7 14 28 35 49 56 70 77 91 98"""

start = int(input("Enter a start range: "))
end = int(input("Enter a end range: "))

i = start

while i <= end:
    if i % 7 == 0 and i % 3 != 0:
        print(i, end = " ")
    i += 1
