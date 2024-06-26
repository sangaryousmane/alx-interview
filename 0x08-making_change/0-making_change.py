#!/usr/bin/python3
""" Make a change needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Make a change to reach a given total
    """
    if total <= 0:
        return 0
    temp = total
    counter = 0
    i = 0
    rev_coins = sorted(coins, reverse=True)
    n = len(coins)
    while temp > 0:
        if i >= n:
            return -1
        if temp - rev_coins[i] >= 0:
            temp -= rev_coins[i]
            counter += 1
        else:
            i += 1
    return counter
