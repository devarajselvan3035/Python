"""
507. Perfect Number
===================
A Perfect Number is a positive integer that is equal to the sum of its pasitive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false
"""


def checkPerfectNumber(num: int) -> bool:
    ans = 0
    idx = 1
    while ans < num and idx < num:
        if num % idx == 0:
            ans += idx

        idx += 1
    print(ans)
    return ans == num


num = 2016
print(checkPerfectNumber(num))
