start_range = input("Enter a starting range: ")
end_range = input("Enter a ending range: ")

ascai_value1 = ord(start_range)
ascai_value2 = ord(end_range)

for i in range(ascai_value1, ascai_value2):
    char = chr(i)
    print("ASCII value of {} is {}".format(char,i))

