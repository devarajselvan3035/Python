"""
459. Repeated Substring Pattern(*)
===============================
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""


def repeatedSubstringPattern(s: str) -> bool:
    len_s = len(s)
    for i in range(1, len(s)):
        if len_s % i == 0:
            subString = s[:i]
            fullString = subString * (len_s // i)
            print(fullString, s)
            if fullString == s:
                return True
    return False


# s = "abcabcabcabc"
# s = "abcabc"
s = "aba"
# s = "ababba"
# s = "ababababab"
print(repeatedSubstringPattern(s))
