#WAP to find the 7th odd number (start from 1)
#Output:
#7th odd number is 13

count = 0
num = 1

while count < 7:
    if num % 2 == 1:
        count += 1
    num += 1

print("7th odd number is:",num-1)
