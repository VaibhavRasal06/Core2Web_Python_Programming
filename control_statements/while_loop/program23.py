"""WAP to print all the character values of the given ASCII value range from the
user
Input : Enter the start of range : 1
Enter end of range: -2
Output : Wrong input
Input : Enter start of range : 65
Enter end of range : 67
Output :
The character of ASCII value 65 is A.
The character of ASCII value 66 is B.
The character of ASCII value 67 is C.
.
.
.
The character of ASCII value 89 is Y."""

start = int(input("Enter the start range: "))
end = int(input("Enter the end range: "))


if start < 65 or start > 89:
    print("Wrong input: Start value should be between 65 and 89.")

elif start > end:
    print("Wrong input: Start range cannot be greater than end range.")

else:
    i = start
    while i <= end:
        char_value = chr(i)
        print("The character of ASCII value {} is {}".format(i, char_value))
        i += 1
