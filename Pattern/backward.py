"""
Write a program to print the following:
4 3 2 1
4 3 2 1
4 3 2 1
4 3 2 1
"""

n = int(input("Enter the size: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{n-j+1} ", end=" ")
    print()