"""
367. Valid Perfect Square (***)
=========================
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
"""


# NOTE: Time Complexity: O(logN) -> Using Binary Search Tree
def isPerfectSquare(num: int) -> bool:
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        if mid**2 == num:
            return True
        if num < mid**2:
            right = mid - 1
        if num > mid**2:
            left = mid + 1
    return False


# NOTE: Time Complexity: O(SQRT(N)) -> Basic for loop with N iterations
def isPerfectSquare1(num: int) -> bool:
    for n in range(1, num):
        if n**2 == num:
            return True
        elif n**2 > num:
            break
    return False


num = 14
print(isPerfectSquare1(num))
