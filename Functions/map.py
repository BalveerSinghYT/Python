"""
String List to Integers List
"""
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print(type(num[2]))


# 1. Convert all string elements in list to integers
# for i in range(len(num)):
#     num[i] = int(num[i])

# print(type(num[2]))


## 2. Using MAP Function, can do same in one line

map_num = list(map(int, num))
print(type(map_num[2]))


"""
Square of elements in a list
"""

# 1. Using Def function
int_num = [1,2,3,4,5]
def seq(a):
    return a*a

sq_list = list(map(seq, int_num))
print(sq_list)

# 2. Using Lambda

lam_list = list(map(lambda x:x*x, int_num))
print(lam_list)


"""
Applying two functions on a list at same time
"""
def sequare(a):
    return a*a

def cube(a):
    return a*a*a

func = [sequare, cube]
print("\nSquare, Cube: ")
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print("  ", val)