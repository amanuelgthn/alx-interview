#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Function that returns the pascal triangle for a given number"""
    triangle = []
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            row.append(binomial_coefficient(i, j))
        triangle.append(row)
    if n <= 0:
        return []
    return triangle


def factorial(n):
    """returns the factorial of n"""
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * factorial(n - 1)


def binomial_coefficient(n, k):
    """function for binomial coefficient"""
    coefficient = 1
    coefficient = factorial(n) // (factorial(k) * factorial(n - k))
    return coefficient
