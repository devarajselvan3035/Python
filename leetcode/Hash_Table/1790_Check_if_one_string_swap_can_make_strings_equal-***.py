"""
1790. check if One String Swap Can Make Strings Equal (***)
======================================================
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
"""

from typing import Dict


def areaAlmostEqual(s1: str, s2: str) -> bool:
    notMatch = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            notMatch.append(i)

    if len(notMatch) == 0:
        return True

    if len(notMatch) == 2:
        i, j = notMatch
        return s1[i] == s2[j] and s2[j] == s1[i]

    return False


def areaAlmostEqual1(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    def count(s: str) -> Dict:
        res: Dict = dict()
        for c in s:
            res[c] = res.get(c, 0) + 1
        return res

    s1Count = count(s1)
    s2Count = count(s2)

    if s1Count == s2Count:
        temp = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp += 1
            if temp > 2:
                return False

    else:
        return False

    return True


s1, s2 = "bank", "kanb"
s1, s2 = "attack", "defend"
# s1, s2 = "kelb", "kelb"
print(areaAlmostEqual(s1, s2))
