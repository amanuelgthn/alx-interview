#!/usr/bin/python3
"""
a program that solves the N queens problem.
"""


from sys import argv

n = argv[1]
if n < 4:
    print('Usage: nqueens N')
    exit(1)
