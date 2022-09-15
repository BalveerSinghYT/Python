"""
To Print the following pattern:
        *********
        **** ****
        ***   ***
        **     **
        *       *
"""
def main():
    n = int(input("Enter the number of rows: "))
    print("*"*n)
    for i in range(n):
        print("*"*((n//2)-i) + " "*(2*i +1) + "*"*((n//2)-i))

if __name__ == "__main__":
    main()