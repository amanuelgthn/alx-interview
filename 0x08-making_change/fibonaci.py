#!/usr/bin/python3

def fib(n):
    first = 1
    second = 1
    value = 0
    if n == 1 or n == 2:
        return first
    if n > 2:
        for i in range(2, n):
            value = first + second
            first = second
            second = value
        return value
    

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))
