list_1 = [1, 2, 3, 4, 5, 6, 7, 8 , 9]

def is_greater5(num):
    return num>5

val = list(filter(is_greater5, list_1))
print(val)


int_num = [1,2,3,4,5]
def seq(a):
    if a*a == 4:
        return True
    return False

sq_list = list(filter(seq, int_num))
print(sq_list)
