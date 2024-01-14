num = int(input("Enter a number: "))
sum_of_factors = 1
i = 2

while i <= num // 2:
    if num % i == 0:
        sum_of_factors += i
    i += 1

if sum_of_factors == n:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

