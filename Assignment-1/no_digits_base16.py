"""
Q3: Write a program to check the no of digits in base 16 using recursion.
"""

def base16_to_decimal_length(x, count=0):
    if x == "":
        return count
    return base16_to_decimal_length(x[1:], count+1)

def validate(x, i=0):
    if i != len(x):
        if x[i] not in "0123456789ABCDEF":
            print("Invalid number")
            return False
        return validate(x, i+1)
    return True

if __name__ == "__main__":
    while True:
        x = input("Enter Hexadecimal no. : ").upper()

        if validate(x):
            print("No. of digits: ", base16_to_decimal_length(x))
            exit()

      