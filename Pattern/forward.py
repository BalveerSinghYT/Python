"""
Write a program to print the following:
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""

n = int(input("Enter the size: "))
i = 1

while i<=n:
    j = 1
    while j <= n:
        print(f"{j} ", end=" ")
        j+=1
    print()
    i+=1