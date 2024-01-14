"""Write a program to check whether the number is a Perfect
number or not.
Input: 496
Output: 496 is a perfect number."""

n = int(input("Enter a number: "))
sum_of_factors = 1
i = 2
while i * i <= n:
  if n % i == 0:
    sum_of_factors += i + n // i
  i += 1

if sum_of_factors == n:
  print(f"{n} is a perfect number.")
else:
  print(f"{n} is not a perfect number.")

