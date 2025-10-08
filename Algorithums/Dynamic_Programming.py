"""
climbing Stairs 
===============
Determine the numbers of distinct ways to climb staircase of n steps by taking either 1 or 2 steps at a time

Inputs n = 4
Outputs: 5
"""

memo = {}
def climbing_stairs_top_down(n:int) -> int:
    if n <= 2:
        return n
    print(f"before : {(n-1), (n-2)}")
    ans = climbing_stairs_top_down(n-1) + climbing_stairs_top_down(n-2)
    print(f"end : {n-1, n-2}")
    return ans

# print(climbing_stairs_top_down(5))

"""
Minimum coin combination
========================
You are given an array of coin values and a target amount of money. Return the minimum number of coins needed to total the target amount. If this isn't possible, return -1. You may assume there's an unlimited supply of each coin.
"""

def find_coins(coins:list, total:int):
    if total in coins:
        return total
    for coin in coins:
        
