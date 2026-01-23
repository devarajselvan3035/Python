"""
67. Add Binary (*)
Given two binary strings a and b, return their sum as a binary strings.

Example 1:
Input: a = '11', b = '1'
Output: '100'
"""


def addBinary(a: str, b: str) -> str:
    return str(bin(int(a, 2) + int(b, 2))[2:1])


def addBinary1(a: str, b: str) -> str:
    if len(a) < len(b):
        return addBinary(b, a)

    res: str = ""
    rem: int = 0
    diff: int = len(a) - len(b)
    b = "0" * diff + b

    for i in range(len(a) - 1, -1, -1):
        add: int = (ord(a[i]) + ord(b[i])) - (2 * ord("0")) + rem
        if add == 2:
            add = 0
            rem = 1
        else:
            rem = 0
        res = str(add) + res
        print(add, res, rem)

    return str(rem) + res if rem == 1 else res


a, b = "1010", "1011"
print(addBinary(a, b))
