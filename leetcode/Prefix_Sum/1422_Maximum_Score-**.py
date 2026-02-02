"""
1422. Maximum Score After Splitting a String (**)(REF:1413)
============================================
Given a string s of zeros and ones, return the maximum score after splitting the string into two
non-empty substrings (i.e, left substring and right substirng)

The score after splitting a string is the number of zeros in the left substring plus the number of
ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3
"""


# HACK: Two Variable Method
def maxScore(s: str) -> int:
    maxVal = 0
    zeros = 0
    ones = s.count("1")

    for i in range(len(s)):
        if int(s[i]) == 0:
            zeros += 1
        else:
            ones -= 1

        maxVal = max(maxVal, zeros + ones)

    return maxVal


# HACK: Two List Method
def maxScore1(s: str) -> int:
    zeorPrefixSum = []
    onePrefixSum = []
    zero, one = 0, 0
    for idx in range(len(s)):
        zeorPrefixSum.append(zero)
        if int(s[idx]) == 0:
            zero += 1
        if int(s[len(s) - idx - 1]) == 1:
            one += 1
        onePrefixSum = [one] + onePrefixSum

    maxVal = 0
    for i in range(1, len(zeorPrefixSum)):
        maxVal = max(maxVal, zeorPrefixSum[i] + onePrefixSum[i])
    return maxVal

    print(zeorPrefixSum)
    print(onePrefixSum)


s = "011101"
# s = "1111"
print(maxScore(s))
