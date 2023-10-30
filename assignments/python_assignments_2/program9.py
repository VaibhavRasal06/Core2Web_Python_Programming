char1 = (input("Enter a character: "))
char2 = (input("Enter a character: "))

char1_assci = ord(char1)
#print(char1_assci)

char2_assci = ord(char2)
#print(char2_assci)

sum_char = char1_assci+char2_assci

if (sum_char % 2 == 0):
    print(sum_char)
else:
    print("No output")
