#!/usr/bin/python3
"""prime_game"""


def isWinner(x, nums):
    """function that returns the name of that won the most rounds"""
    maria = 0
    ben = 0
    bool = True
    for num in nums:
        j = 2
        if num == 1:
            ben += 1
        if num == 2:
            maria += 1
        for number in nums:
            if number // num == 0:
                nums.pop(number)
        if isPrime(num, 2):
            if bool:
                maria += 1
                bool = False
            else:
                ben += 1
                bool = True
    """ print("Maria: {}, Ben: {}".format(maria, ben)) """
    if ben > maria:
        return "Ben"
    return "Maria"


def isPrime(num, i):
    """"function to check if a prime number is prime"""
    if (num == 1 or num == 0):
        return False
    if (num == i):
        return True
    if (num % i == 0):
        return False
    i += 1
    return isPrime(num, i)
