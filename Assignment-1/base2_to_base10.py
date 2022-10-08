"""
Q1: Write a program to Convert a number from base 2 to base 10 using recursion.
"""
def convert_recursion(x, count, sum=0):
    d = x % 10
    sum = sum + (2**count)*d
    if x == 1:
        return sum
    return convert_recursion(x//10, count+1, sum)

def validate(x):
    while x != "":
        if x[0] not in "01":
            print("Invalid input")
            return False
        return validate(x = x[1:])
    return True

if __name__ == "__main__":
    while True:
    
        n  = input("Enter Binary no. : ")

        if validate(n):
            print("Decimal no. : ", convert_recursion(int(n), 0))
            exit()
