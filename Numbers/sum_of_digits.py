"""
Aim: Write a program to find the sum of digits of a number, without using slicing & array/list.

Example:
    Input: 12345
    Output: 15
"""

sum = 0
x = int(input("Enter a number: "))
for i in range(len(str(x))):
    d = x % 10
    x = x // 10
    sum = sum + d

print("Sum of digits: ", sum)