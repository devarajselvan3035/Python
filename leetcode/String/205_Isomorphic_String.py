"""
205. Isomorphic strings
========================
Given two strings s and t, determine if they are isomorphic.

Two string s and t are isomorphic if the characters is s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order
of chracters. No two chracters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true
"""


def isIsomorphic(s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


def isIsomorphic1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    str_dict = {}
    for sl, tl in zip(s, t):
        if tl not in str_dict:
            if sl in str_dict.values():
                return False
            str_dict[tl] = sl
        elif str_dict[tl] != sl:
            return False
    return True


# s, r = "foo", "bar"
s, r = "babc", "baba"
print(isIsomorphic(s, r))
