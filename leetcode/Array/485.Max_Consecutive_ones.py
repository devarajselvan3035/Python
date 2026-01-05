"""
Given a binary array nums, return the maximum number of consecutive 1's in the array

Example 1
Input: nums = [1,1,0,1,1,1]
Output: 3

Example 2
Input: nums = [1,0,1,1,0,1]
Output: 2
"""


def findMaxConsecutiveOnes(nums: list) -> int:
    res, count = 0, 0
    idx = 0
    while idx < len(nums):
        if nums[idx] == 1:
            count += 1
        else:
            res = max(res, count)
            count = 0
        print(res, count)
        idx += 1

    return max(res, count)


# nums = [1, 1, 0, 1, 1, 1, 0, 1]
nums = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums))
