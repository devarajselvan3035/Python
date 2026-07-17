"""
905. Sort Array By Parity (**)
=========================

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisffies this condition

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""

from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


def sortArrayByParity1(nums: List[int]) -> List[int]:
    return sorted(nums, key=lambda x: x % 2)


nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))
