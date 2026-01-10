"""
392. Is Subsequence (TP)
===================
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


def isSubsequence(s: str, t: str) -> bool:
    si, ti = 0, 0
    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:
            si += 1
        ti += 1
    return si == len(s)


# s, t = "abc", "ahbgdc"
s, t = "axc", "ahbgdc"
print(isSubsequence(s, t))
