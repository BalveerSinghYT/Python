"""
    To Print:
    *
   ***
  *****
 *******
 ....... so on
"""
n = int(input("Enter the size of Pyramid: "))

for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    c = 2*i + 1
    print("*"*c)