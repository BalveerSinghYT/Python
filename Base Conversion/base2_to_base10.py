x = int(input("Base2: "))
len_x = len(str(x))

def valid():
    flag = False

    if '0' or '1' in str(x):
        flag = True

    return flag

def convert(flag, x):
    """
    2^4x1 + 2^3x0 + 2^2x1 + 2^1x1 + 2^0x0
    """
    sum = 0
    for i in range(0, len_x):
        d = x % 10
        sum = sum + (2**i)*d
        x = x // 10
    
    print('Base10:', sum)

if __name__ == "__main__":
    flag = valid()
    convert(flag, x)

