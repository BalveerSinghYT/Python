"""
Reduce is a function that takes a function and a list as arguments, and returns a single value as result.
The function is called with a lambda function and a list and a new reduced result is returned.
This performs a repetitive operation over the pairs of the list.

Syntax:
    reduce(function, sequence)
    function - function that is called for each pair of the list
    sequence - list of elements which is to be reduced

Example:
    reduce(lambda x, y: x+y, [1,2,3,4,5])
    # (((1+2)+3)+4)+5
    # (((3)+3)+4)+5
    # (((6)+4)+5)
    # (((10)+5))
    # 15
"""

# 1. Traditional Approach to add elements of a list

from functools import reduce


num_list = [1, 2, 3, 4, 5, 6]
sum = 0
for i in num_list:
    sum = sum + i

print(sum)

# 2. Same thing in one line using reduce

sum = reduce(lambda x,y: x+y, num_list)
print(sum)