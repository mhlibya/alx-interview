#!/usr/bin/python3
"""
Making change problem solution
"""

def makeChange(coins, total):
    """
    Making change function
    """
    mo = [float('inf')] * (total + 1)
    mo[0] = 0
    coins.sort()

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                mo[i] = min(mo[i], mo[i - coin] + 1)
    return mo[total] if mo[total] != float('inf') else -1
