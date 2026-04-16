"""
1005. Maximize Sum of Array After K Negations
=============================================
Given an integer array nums and an integer k, modify the array in the following way:

    choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].

Example 2:
Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
"""

from typing import List


def largestSumAfterKNegations(nums: List[int], k: int) -> int:

    nums.sort()
    i = 0
    while k > 0:
        if i == len(nums) or nums[i] >= 0:
            break
        else:
            nums[i] = -nums[i]
            i += 1
        k -= 1

    nums.sort()
    while k > 0:
        nums[0] = -nums[0]
        k -= 1

    return sum(nums)


nums, k = [3, -1, 0, 2], 3
nums, k = [2, -3, -1, 5, -4], 2
nums, k = [4, 2, 3], 1
nums, k = [-8, 3, -5, -3, -5, -2], 6
print(largestSumAfterKNegations(nums, k))
