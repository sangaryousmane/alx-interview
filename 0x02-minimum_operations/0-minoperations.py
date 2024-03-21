#!/usr/bin/python3
""" A function that calculates the fewest number
of operations needed to result in exactly n H characters in the file
"""
import math


def minOperations(n):
    """ A function that calculates the fewest number
    of operations needed to result in exactly n H characters in the file"""
    if not isinstance(n, int):
        return 0

    operations = 0
    i = 2
    while i <= n:
        if not (n % i):
            n = int(n / i)
            operations += i
            i = 1
        i += 1
    return operations
