"""
Q5: Write a program to convert a base 16 number to base 10 number.
"""

def base16_to_decimal(x, count=0, sum=0):

    if x == "":
        return sum

    if x[0] in "ABCDEF":
        d = ord(x[0]) - 55
    else:
        d = int(x[0])

    sum = sum + (16**count)*d

    return base16_to_decimal(x[1:], count+1, sum)

def validate(x):
    while x != "":
        if x[0] not in "0123456789ABCDEF":
            print("Invalid number")
            return False
        return validate(x = x[1:])
    return True

if __name__ == "__main__":
    while True:
        x = input("Enter Hexadecimal no. : ").upper()
        if validate(x):
            print("Decimal no. : ", base16_to_decimal(x))
            exit()