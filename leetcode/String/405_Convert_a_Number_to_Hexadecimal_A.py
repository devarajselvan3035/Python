"""
405. Convert a Number to hexadecimal(*)
====================================
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"
"""


def toHex(num: int) -> str:
    if num == 0:
        return "0"
    if num < 0:
        num += 2**32
    hex_str = "abcdef"
    res = ""
    while num >= 16:
        rem = num % 16
        num = num // 16
        if rem > 9:
            res = hex_str[rem - 10] + res
        else:
            res = str(rem) + res
    return str(num) + res if num < 10 else hex_str[num - 10] + res


print(toHex(26))
print(toHex(-1))
print(toHex(16))
