"""
Given an integer array nums, return the third distict maximum number in this array. If the third maximum does not exist, return the maximum number

Input: nums = [2, 2, 3, 1]
Output: 1

Input: nums = [1, 2]
Output: 2
"""


def thirdMax(nums: list) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)
    return nums[2] if len(nums) > 2 else max(nums)


nums = [2, 2, 3, 1]
nums = [1, 2]
print(thirdMax(nums))
