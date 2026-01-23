"""
504. Base 7
============
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"
"""


def base7(num: int) -> str:
    res = ""
    mul = 1

    if num < 0:
        num = -1 * num
        mul = -1

    while 7 <= num or num <= -7:
        rem = num % 7
        res = str(rem) + res
        num //= 7
        print(rem, num)
    return str(mul * num) + res


# print(base7(100))
print(base7(-8))
