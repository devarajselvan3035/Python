"""
344. Reverse String
===================
Write a function that reverses a string. The input string is given as an array of characters s.

you must do this by modifying the input array in-place with 0(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

from typing import List


def reverseString(s: List[str]) -> None:
    # Do no return anything, modify s in-place instead.
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    print(s)


s = ["h", "e", "l", "a", "l", "o"]
reverseString(s)
