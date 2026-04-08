"""
1624. Larget Substring Between Two Equal Characters (**)
===================================================

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
"""


def maxLength(s: str) -> int:
    res = -1
    sIdx = {}
    for i, c in enumerate(s):
        if c not in sIdx:
            sIdx[c] = i
        else:
            length = i - sIdx[c] - 1
            res = max(res, length)

    return res


s = "abca"
s = "cbzxy"
print(maxLength(s))
