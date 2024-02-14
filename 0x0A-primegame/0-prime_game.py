#!/usr/bin/python3
"""prime_game"""


def isWinner(x, nums):
    """function that returns the name of that won the most rounds"""
    maria = 0
    ben = 0
    for num in nums:
        j = 2
        if num == 1:
            ben += 1
        if num == 2:
            maria += 1
        for number in nums:
            if number // num == 0:
                nums.pop(number)
        
 