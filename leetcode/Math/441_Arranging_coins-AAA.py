"""
441 Arranging Coins (***)
===================
You have n coins and you want to build a staircase with these coins. the staircase consists of k rows wher the ith row has exactly i coins. The last row of the staircase may be incomplete.

give the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
1 $
2 $ $
3 $ $

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

1 $
2 $ $
3 $ $ $
4 $ $
"""


# NOTE : Time Complexity: O(log N) -> Using binary search tree
def arrangeCoins(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = (left + right) // 2
        total = mid * (mid + 1) // 2

        if total == n:
            return mid
        elif total < n:
            left = mid + 1
        elif total > n:
            right = mid - 1
    return right


# NOTE: Time Complexity: O(N) -> basic for loop
def arrangeCoins1(n: int) -> int:
    total = 0
    for i in range(1, n):
        total += i
        if total > n:
            return i - 1


n = 8
print(arrangeCoins(n))
