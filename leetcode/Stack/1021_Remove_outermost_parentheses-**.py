"""
1021. Remove Outermost Parentheses (**)
=======================================
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
- For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""


# HACK: Less time complexity
def removeOuterParentheses(s: str) -> str:
    res = []
    balance = 0
    for c in s:
        if c == "(":
            if balance > 0:
                res.append(c)
            balance += 1
        else:  # c == ')'
            balance -= 1
            if balance > 0:
                res.append(c)

    return "".join(res)


# HACK: More time complexity
def removeOuterParentheses1(s: str) -> str:
    stack = ""
    count = 0
    ans = ""
    for pt in s:
        if pt == "(":
            stack += pt
            count += 1
        elif pt == ")":
            stack += pt
            count -= 1

        if count == 0:
            ans += stack[1:-1]
            stack = ""
    return ans


par = "(()())(())"
# par = "(()())(())(()(()))"
# par = "()()"
par = "((()())(()()))"
print(removeOuterParentheses(par))
