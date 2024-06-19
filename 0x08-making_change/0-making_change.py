#!/usr/bin/python3
""" Make a change needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Make a change to reach a given total
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
