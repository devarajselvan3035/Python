"""
541. Reverse String II
======================
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
"""


def reverseStr(s: str, k: int) -> str:
    res = ""
    idx = 0
    if len(s) <= k:
        return s[::-1]
    if len(s) <= 2 * k:
        subStr1 = s[idx : idx + k]
        substr2 = s[idx + k :]
        return subStr1[::-1] + substr2

    while idx < len(s):
        subStr1 = s[idx : idx + k]
        substr2 = s[idx + k : idx + (2 * k)]
        res += subStr1[::-1]
        res += substr2

        idx = idx + (2 * k)
    return res + s[idx:]


# s, k = "abcdefg", 2
# s, k = "abcd", 2
s, k = "abcdef", 3
print(reverseStr(s, k))
