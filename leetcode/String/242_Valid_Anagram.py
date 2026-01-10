"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = 'anagram', t = 'nagaram'
Output: True
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_dict, t_dict = {}, {}
    for sl, tl in zip(s, t):
        if sl not in s_dict:
            s_dict[sl] = 1
        else:
            s_dict[sl] += 1

        if tl not in t_dict:
            t_dict[tl] = 1
        else:
            t_dict[tl] += 1

    return s_dict == t_dict


# s, t = "anagram", "nagaram"
s, t = "rat", "car"
print(isAnagram(s, t))
