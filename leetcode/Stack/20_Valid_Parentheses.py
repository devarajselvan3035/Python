"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""


def isValid(s: str) -> bool:
    part_dict = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif part_dict[stack[-1]] != c:
            stack.append(c)
        else:
            stack.pop()
    return True if len(stack) == 0 else False


# s = "()[]{}"
# s = "([])"
s = "([{"
print(isValid(s))
