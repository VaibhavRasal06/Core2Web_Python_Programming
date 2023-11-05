start = int(input("Enter a starting number: "))
end = int(input("Enter a ending value: "))

count = 0

for i in range(start,end):
    if (i % 2 == 1):
        count = count + 1
print(count**count)
        
