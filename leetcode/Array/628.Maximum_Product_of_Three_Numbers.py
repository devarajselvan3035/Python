"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

"""

from typing import List


def maximumProduct(nums: List[int]) -> int:
    sort_nums = sorted(nums, reverse=True)
    r1 = sort_nums[0] * sort_nums[1] * sort_nums[2]
    r2 = sort_nums[-1] * sort_nums[-2] * sort_nums[0]
    return max(r1, r2)


# nums = [1, 2, 3, 4]
# nums = [-1, -2, -3]
nums = [-100, -98, -1, 2, 3, 4]
print(maximumProduct(nums))
