"""
409. Longest Palindrome(*)(DICT)
=======================
Given a string s which consists of lowercase or uppercase letters, return the length of the logest palindrome that can be build with those letters.

Letters are case sensitive for example, "Aa" is not considered a palindrome

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""


def logestPalindrome(s: str) -> int:
    res = 0
    odd = 0
    count_s = {}
    for c in s:
        count_s[c] = count_s.get(c, 0) + 1

    for c in list(count_s.values()):
        res += (c // 2) * 2
        if c % 2 == 1:
            odd = 1

    return res + odd


def logestPalindrome1(s: str) -> int:
    res = 0
    maxval = 0
    s_count = {}
    for c in s:
        s_count[c] = s_count.get(c, 0) + 1

    for count in list(s_count.values()):
        if count % 2 == 1:
            res -= maxval
            maxval = max(count, maxval)
            res += maxval
        if count % 2 == 0:
            res += count
    return res


s = "abccccdd"
s = "aa"
print(logestPalindrome(s))
