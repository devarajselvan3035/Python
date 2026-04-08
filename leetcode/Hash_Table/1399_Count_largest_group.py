"""
1399. Count Largest Group
=========================

You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
"""


def countLargestGroup(n: int) -> int:
    sumCount = {}

    def digit_sum(val: int) -> int:
        res = 0
        while val > 0:
            res += val % 10
            val //= 10

        return res

    for i in range(1, n + 1):
        idx = digit_sum(i)
        if idx not in sumCount:
            sumCount[idx] = [i]
        else:
            sumCount[idx].append(i)

    maxLen = len(max(sumCount.values(), key=len))

    return len([val for val, arr in sumCount.items() if len(arr) == maxLen])


n = 2
print(countLargestGroup(n))
