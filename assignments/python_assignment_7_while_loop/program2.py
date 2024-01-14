"""Write a program to check whether the number is a Prime
number or not. (2332)
Input:2332
Output:2332 is not a prime number"""

num = int(input("Enter a number: "))
i = 2
while(i <= num//2):
  if(num % i == 0):
     print(num, "is not a prime number")
     break
  i = i + 1
else:
  print(num, "is a prime number")

