"""
Write a program to find the reverse of a number, without using slicing & array/list.
Example:
Input: 12345
Output: 54321
"""

x = int(input("Enter a Number: "))
output = ""

for i in range(len(str(x))):
    m = x % 10      # will return the last digit or reminder 
    x = x // 10     # '//' will return the floor value after division
    output += f"{m}"

print("Reverse: ", output)