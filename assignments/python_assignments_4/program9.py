start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))

count = 0

for i in range(start,end+1):
    if i < 0:
        count += 1
print(count)

