#!/usr/bin/python3
"""
Given a pile of coins of different values, determining the fewest number of
coins needed to meet a given amonnt total
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed to meet a
    given amount total
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
