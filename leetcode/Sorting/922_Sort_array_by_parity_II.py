"""
922. Sort Array By Parity II
============================

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and wherever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]
"""

from typing import List


def sortArrayByParityII(nums: List[int]) -> List[int]:
    yes = []
    no = []

    for i in range(len(nums)):
        if (nums[i] % 2 == 0 and i % 2 == 0) or (nums[i] % 2 == 1 and i % 2 == 1):
            yes.append(nums[i])
        else:
            no.append(nums[i])

    return no + yes


nums = [4, 2, 5, 7]
nums = [2, 3]
print(sortArrayByParityII(nums))
