#!/usr/bin/python3
"""
Minimum number of operations
"""


def minOperations(n):
    """
    function that calculates minimum number of operations
    needed to result in exactly n H operations in the file
    """

    if n <= 1 or type(n) is not int:
        return 0
    num_op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            num_op += i
            i = 1
        i += 1
    return num_op
