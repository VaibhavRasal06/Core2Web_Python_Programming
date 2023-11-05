start = int(input("Enter a starting number: "))
end = int(input("Enter a ending value: "))

if start > end:
    print("Wrong Input")

else:
    
    for i in range(start, end+1):
        char = chr(i)
        print("The character of ASCII value {} is {}.".format(i,char))
