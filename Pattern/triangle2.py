"""
Write a program to print the following:
    1
    2 3
    4 5 6
    7 8 9 10
"""

n = int(input("Enter the size: "))
k = 1

for i in range(1, n):
    for j in range(1, i+1):
        print(f"{k} ", end="")
        k+=1
    print()