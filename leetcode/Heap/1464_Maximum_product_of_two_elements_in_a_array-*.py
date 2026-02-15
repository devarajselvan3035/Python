"""
1464. Maximum Products of Two Elements in an Array (*)
==================================================
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
Input: nums = [3,7]
Output: 12
"""

import heapq
from typing import List


def maxProduct(nums: List[int]) -> int:
    heapq.heapify_max(nums)
    m1 = heapq.heappop_max(nums)
    m2 = heapq.heappop_max(nums)
    return (m1 - 1) * (m2 - 1)


def maxProduct1(nums: List[int]) -> int:
    nums.sort(reverse=True)
    m1 = nums[0]
    m2 = nums[1]
    return (m1 - 1) * (m2 - 1)


nums = [3, 4, 5, 2]
nums = [1, 5, 4, 5]
print(maxProduct(nums))
