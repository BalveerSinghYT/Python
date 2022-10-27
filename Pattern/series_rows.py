"""
Write a program to print the following:
1 2 3
4 5 6
7 8 9
"""

n, r = map(int, input("Enter the size & row: ").split())

j = 1
i = 1

for i in range(1, n+1):
    print(f"{i} ", end=" ")

    if i % 3 == 0:
        print()

