"""
Q6: Write a program to count total number of bits in a number using recursion.
"""

def no_of_bits(x, count=0):
    if x == 0:
        return count
    return no_of_bits(x//2, count+1)

if __name__ == "__main__":
    while True:
        x = int(input("Enter a number: "))
        print("No. of bits: ", no_of_bits(x))