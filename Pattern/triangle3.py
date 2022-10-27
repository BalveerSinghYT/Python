"""
Write a program to print the following:
    1
    2 3
    3 4 5
    4 5 6 7
"""

n = int(input("Enter the size of triangle: "))

for i in range(1, n+1):
    k = i
    for j in range(1, i+1):
        print(k, end=" ")
        k+=1
        
    print()