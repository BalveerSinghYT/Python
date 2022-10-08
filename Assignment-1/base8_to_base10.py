"""
Q4: Write a program to convert a base 8 number to base 10 number.
"""

def base8_to_decimal(x, count=0, sum=0):

    d = x % 10
    sum = sum + (8**count)*d

    if x == 0:
        return sum
    return base8_to_decimal(x//10, count+1, sum)

def validate(x):
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
            print("Decimal no. : ", base8_to_decimal(int(x)))
            exit()
