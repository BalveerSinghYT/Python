"""
Q2: Write a program to check the no of digits in base 8 using recursion.
"""

def no_digits(x, count=0):
    if x == 0:
        return count
    return no_digits(x//8, count+1)

def validate(x, i=0):
    while x != "":
        if x[0] not in "01234567":
            print("Invalid number")
            return False
        return validate(x = x[1:])
    return True
    
if __name__ == "__main__":
    while True:
        x = input("Enter Octal no. : ")

        if validate(x):
            print("No. of digits: ",no_digits(int(x)))
            exit()
