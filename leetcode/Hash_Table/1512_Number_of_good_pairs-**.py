"""
1512. Number of Good pairs
==========================
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
"""


def numIdenticalPairs(nums: List[int]) -> int:
    numsCount = {}
    res = 0
    for n in nums:
        numsCount[n] = numsCount.setdefault(n, 0) + 1

    for cot in numsCount.values():
        # NOTE: Important formula
        """
        if n=5
        Instead of using below method in for loop,
        1+2+3+4 = 10

        You can use simeple formula for that
        (n)*(n-1) // 2 = 5*4//2 = 20//2 = 10

        """
        res += (cot * (cot - 1)) // 2

    return res


nums = [1, 2, 3, 1, 1, 3]
# nums = [1, 1, 1, 1]
# nums = [1, 2, 3]
print(numIdenticalPairs(nums))
