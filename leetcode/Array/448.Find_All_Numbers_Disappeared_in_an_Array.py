"""
Given an array nums of n integers where nums[i] is in the range [1,n], return an array of all the integers in the range [1, n] that do not appear in nums

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]
"""


def findDisappearedNumber(nums: list) -> list:
    return list(set(range(1, len(nums) + 1)) - set(nums))


def findDisappearedNumber2(nums: list) -> list:
    res = []
    for v in range(1, len(nums) + 1):
        if v not in nums:
            res.append(v)
    return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumber(nums))
