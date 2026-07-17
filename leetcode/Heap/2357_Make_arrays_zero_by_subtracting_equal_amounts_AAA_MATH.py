"""
2357. Make Array Zero by Substracting Equal Amounts (***)(MATH)
===================================================
You are given a non-negative integer array nums. In one operation, you must:
- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

Example 1:
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

Example 2:
Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
"""

from typing import List


def minimumOperations(nums: List[int]) -> int:
    # Create a set of all numbers to get unique values
    unique_numbers = set(nums)

    # If 0 is in the set, remove it because
    # subtracting from 0 isn't an operation.
    if 0 in unique_numbers:
        unique_numbers.remove(0)

    # The number of operations is the number of unique positive values
    return len(unique_numbers)


def minimumOperations1(nums: List[int]) -> int:
    nums.sort()
    l, res = 0, 0
    while l < len(nums):
        if nums[l] == 0:
            l += 1
        else:
            minVal = nums[l]
            res += 1
            for idx in range(l, len(nums)):
                nums[idx] = nums[idx] - minVal
    return res


nums = [1, 5, 0, 3, 5]
# nums = [0]
print(minimumOperations(nums))
