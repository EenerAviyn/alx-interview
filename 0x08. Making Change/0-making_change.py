#!/usr/bin/python3
"""Function to determine fewest number of coins needed
   to meet given amount total"""


def makeChange(coins, total):
    """Function that takes list of coins and uses
       that to calculate amount of change that total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
