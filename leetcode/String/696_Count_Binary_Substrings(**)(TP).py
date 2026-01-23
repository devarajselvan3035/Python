"""
696. Count Binary Substrings(**)(TP)
============================
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""


def countBinarySubstring(s: str) -> int:
    cur, pre = 0, 0
    l, r = 0, 0
    count = 0
    res = 0
    while r <= len(s):
        if r == len(s) or s[l] != s[r]:
            pre = cur
            cur = count
            res += min(pre, cur)
            l = r
            count = 0
        count += 1
        r += 1
    return res


# s = "00110011"
s = "10101"
print(countBinarySubstring(s))
