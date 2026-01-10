"""
415. Add Strings(*)
================
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string

You mus solve the problem without using any built-in libraty for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


def addStrings(num1: str, num2: str) -> str:
    res = ""
    rem = 0
    if len(num1) < len(num2):
        return addStrings(num2, num1)
    diff = len(num1) - len(num2)
    num2 = ("0" * diff) + num2
    for i in range(len(num1) - 1, -1, -1):
        add = (ord(num1[i]) + ord(num2[i])) - (2 * ord("0"))
        add += rem
        if add > 9:
            rem = add // 10
            add = add % 10
        else:
            rem = 0
        res = str(add) + res
    return str(rem) + res if rem != 0 else res


# num1, num2 = "11", "123"
# num1, num2 = "456", "77"
num1, num2 = "1", "9"
print(addStrings(num1, num2))


#
# for i in range(10):
#     print(ord(str(i)))
