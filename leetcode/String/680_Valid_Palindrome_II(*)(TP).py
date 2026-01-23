"""
680. Valid Palindrome II(*)(TP)
========================
Given a string s, return true if the s can be palindrome after deleting at most one chracter form it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""


def validPalindrome(s: str) -> bool:

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            subL, subR = s[l + 1 : r + 1], s[l:r]
            return subL[::-1] == subR[::-1]
        l, r = l + 1, r - 1
    return True


# 470 / 477 testcases are passed
def validPalindrome1(s: str) -> bool:
    l, r = 0, len(s) - 1
    flag = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif flag == 0 and s[l + 1] == s[r]:
            l += 1
            flag = 1
        elif flag == 0 and s[r - 1] == s[l]:
            r -= 1
            flag = 1
        else:
            return False
    return True


# s = "aba"
# s = "abca"
s = "abc"
print(validPalindrome(s))
