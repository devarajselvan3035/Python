"""
387. First Unique Character in a String (DICT)
=======================================
Given a string s, find the first non-repeating Character in it and return its index.
If it does not exit, return -1

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


def firstUniqChar(s: str) -> int:
    unique_dict = {}
    for l in s:
        unique_dict[l] = unique_dict.get(l, 0) + 1
    for i, l in enumerate(s):
        if unique_dict[l] == 1:
            return i
    return -1


def firstUniqChar1(s: str) -> int:
    unique_dict = {}
    first = []
    for i, l in enumerate(s):
        if l not in unique_dict:
            first.append(i)
            unique_dict[l] = i
        else:
            unique_dict[l] = i

    for f, l in zip(first, list(unique_dict.values())):
        if f == l:
            return f
    return -1


# s = "leetcode"
s = "aabb"
print(firstUniqChar(s))
