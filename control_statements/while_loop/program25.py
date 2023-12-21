"""WAP that prints all Positive numbers from a given range.
Input: Start: -7
End: 8
Output: 1 2 3 4 5 6 7"""

start = int(input("Enter a start range: "))
end = int(input("Enter a end range: "))

if start > 1:
    print("Please, enter a start a value less than or equal to 1")

else:

    i = start
    while i <= end:
        if i > 0:
            print(i, end = " ")
    i += 1
