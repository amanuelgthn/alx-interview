#!/usr/bin/python3
"""
Minimum number of operations
"""


def minOperations(n):
    """
    function that calculates minimum number of operations
    needed to result in exactly n H operations in the file
    """

    if n <= 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 3
    num_operations = 3
    copied = 1
    num_chars = 3
    for i in range(2, n):
        if num_chars + copied == n:
            num_chars += copied
            num_operations += 1
            return num_operations
        else:
            copied = num_chars
            num_operations += 1
            num_chars += copied
            num_operations += 1
            if num_chars >= n:
                return num_operations
    return 0
