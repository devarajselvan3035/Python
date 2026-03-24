"""
771. Jewels and Stones
======================
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each Character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stones form "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""


def numJewelsInStones(jewels: str, stones: str) -> int:
    stonesCount = {}
    res = 0
    for s in stones:
        stonesCount[s] = stonesCount.setdefault(s, 0) + 1

    for j in jewels:
        if j in stonesCount:
            res += stonesCount[j]

    print(stonesCount)
    return res


jewels, stones = "aA", "aAAbbbb"
jewels, stones = "z", "ZZ"
print(numJewelsInStones(jewels, stones))
