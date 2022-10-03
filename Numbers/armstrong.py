"""
Aim: Write a program to check whether a number is Armstrong or not, without using slicing & array/list.

Definition: A number is called Armstrong number if it is equal to the sum of cubes of its digits.
    example: 
        153 = 1^3 + 5^3 + 3^3
"""
sum = 0
x = int(input("Enter a number: "))
temp = x

for i in range(len(str(x))):
    d = x % 10
    x = x // 10
   
    sum = sum + (d*d*d)

if sum == temp:
    print("Input nuber is an armstrong number")
else:
    print("Not an armstrong number")
