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

    coins.sort(reverse=True)
    print(coins)