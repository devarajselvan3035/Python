"""
1614. Maximum Nesting Depth of the Parentheses
==============================================
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3
"""


def maxDepth(s: str) -> int:
    ans = 0
    count = 0
    for c in s:
        if c == "(":
            count += 1
            ans = max([ans, count])
        elif c == ")":
            count -= 1
    return ans


s = "(1+(2*3)+((8)/4))+1"
s = "(1)+((2))+(((3)))"
s = "()(())((()()))"
print(maxDepth(s))
