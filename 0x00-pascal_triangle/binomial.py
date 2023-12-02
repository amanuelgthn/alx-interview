#!/usr/bin/python3
"""
Binomial funtion
"""

import sys
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n* factorial(n -1)
print(factorial(3))

def binomial_coefficient(n, k):
    coefficient = 1
    coefficient = factorial(n) // (factorial(k) * factorial(n - k))
    return coefficient

print(binomial_coefficient(4,2))
    
