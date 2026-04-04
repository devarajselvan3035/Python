"""
914. X of a Kind in a Deck of Cards
===================================
You are given an integer array deck where deck[i] represents the number written on the ith card.
Partition the cards into one or more groups such that:

    Each group has exactly x cards where x > 1, and
    All the cards in one group have the same integer written on them.

Return true if such partition is possible, or false otherwise.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
"""

from typing import List


def hasGroupsSizeX(deck: List[int]) -> bool:
    deckCount = {}
    for card in deck:
        deckCount[card] = deckCount.setdefault(card, 0) + 1

    counts = sorted(deckCount.values())
    for c in counts:
        if c == 1 or c % counts[0] != 0:
            return False
    return True


# deck = [1, 2, 3, 4, 4, 3, 2, 1]
deck = [1, 1, 1, 2, 2, 2, 3, 3]
deck = [1, 1, 2, 2, 2, 2]
deck = [0, 0, 0, 1, 1, 1, 2, 2, 2]
print(hasGroupsSizeX(deck))
