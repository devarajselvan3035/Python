"""
1365. How Many Numbers Are Samller Than the Current Number
==========================================================
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer is an array

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""

from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    arr = [0] * 101

    for n in nums:
        arr[n] += 1

    return [sum(arr[:n]) for n in nums]


def smallerNumbersThanCurrent1(nums: List[int]) -> List[int]:
    res = []
    for idx in range(len(nums)):
        subNums = nums[:idx] + nums[idx + 1 :]
        tol = 0
        for num in subNums:
            if num < nums[idx]:
                tol += 1

        res.append(tol)
    return res


nums = [8, 1, 2, 2, 3]
# nums = [6, 5, 4, 8]
# nums = [7, 7, 7, 7]
print(smallerNumbersThanCurrent(nums))
