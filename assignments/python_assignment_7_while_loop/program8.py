"""Write a program to check whether the number is a
Palindrome number or not.
Input: 2332
Output: 2332 is a palindrome number"""

# Input: Get the number from the user
num = int(input("Enter a number: "))

# Convert the number to a string
num_str = str(num)

# Initialize variables
length = len(num_str)
is_palindrome = True
i = 0

# Use while loop for comparison
while i < length // 2:
    if num_str[i] != num_str[length - i - 1]:
        is_palindrome = False
        break
    i += 1

# Check if the number is a palindrome
if is_palindrome:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")

