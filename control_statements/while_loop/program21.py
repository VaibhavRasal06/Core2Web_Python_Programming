"""Write a Program to print all Even numbers from a given range.
Input :
Start = 10;
End = 20;
Output:
10 12 14 16 18"""

i = 10

while i < 20:
    if i % 2 == 0:
        print(i)
    i += 1
