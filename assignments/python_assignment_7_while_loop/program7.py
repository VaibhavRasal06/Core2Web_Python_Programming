"""Write a program to reverse the given number.
Input:43521
Output: 12534"""

input_no = int(input("Enter a number: "))

rev_no = 0

while input_no > 0:

    num = input_no % 10

    rev_no = (rev_no * 10) + num

    input_no = input_no // 10

print("The Reversed Number is: ", rev_no)
