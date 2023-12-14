#!/usr/bin/python3
"""
print list of triangular numbers from a random list of 50 numbers
"""


from random import randint
list = []
for i in range(50):
    list.append(randint(1, 1000))


def isTriangular(num):
    """
    check if num is a triangular number
    """
    sum = 0
    if num == 0 or num == 1:
        return True
    for i in range(num):
        sum += i
        if sum == num:
            return True
    return False


triangular_list = []
for i in list:
    print(i)
    if isTriangular(i):
        triangular_list.append(i)
print(triangular_list)
