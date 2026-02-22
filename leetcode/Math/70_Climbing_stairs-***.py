"""
70. Climbing Stairs (***)
===================
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


# NOTE: Basically below problem make fibanacci series
# moves    : 1 2 3 5 8 13 (fibanacci series)
# Steps(n) : 1 2 3 4 5 6
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev = 1
    curd = 2
    for _ in range(2, n):
        prev, curd = curd, prev + curd

    return curd


n = 5
print(climbStairs(n))
