"""
724. Find Pivot Index (***)
=====================
Given an array of integers nums, calculate the pivot indes of this arryy.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal
to the sum of all the numbers strictly to the index's right

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the
right edge of the array.

Return the leftmost pivot index. if no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""

from typing import List, runtime_checkable


# HACK: It is important method for PREFIX SUM
def pivotIndex(nums: List[int]) -> int:
    left = 0
    right = sum(nums)

    for i, num in enumerate(nums):
        right -= num
        if left == right:
            return i
        left += num

    return -1


def pivotIndex1(nums: List[int]) -> int:
    prefixSum = []
    temp = 0
    for n in nums:
        temp += n
        prefixSum.append(temp)

    print(prefixSum)

    for i in range(len(nums)):
        left = 0 if i == 0 else prefixSum[i - 1]
        right = 0 if i == len(nums) - 1 else (prefixSum[len(nums) - 1] - prefixSum[i])
        if left == right:
            return i
    return -1


nums = [1, 7, 3, 6, 5, 6]
# nums = [2, 1, -1]
# nums = [1, 2, 3]
print(pivotIndex(nums))
