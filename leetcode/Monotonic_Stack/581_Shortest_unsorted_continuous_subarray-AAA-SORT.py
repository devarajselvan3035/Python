"""
581. Shortest Unsorted Continuous Subarray (***)(SORT)
==========================================
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0
"""

from typing import List


def findUnsortedSubarray2(nums: List[int]) -> int:
    sortNums = sorted(nums)
    left, right = -1, -1
    for idx in range(len(nums)):
        if nums[idx] != sortNums[idx]:
            if left == -1:
                left = idx
            right = idx + 1

    return right - left


def findUnsortedSubarray(nums: List[int]) -> int:
    n = len(nums)
    left_boundary = n
    stack = []

    # First pass: find the left boundary of the unsorted subarray
    # Maintain a non-decreasing stack. When a smaller element is encountered,
    # it means elements from the stack (which should be to the left) are out of place.
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            left_boundary = min(left_boundary, stack.pop())
        stack.append(i)

    stack = []
    right_boundary = -1

    # Second pass: find the right boundary of the unsorted subarray
    # Maintain a non-increasing stack from the right. When a larger element
    # is encountered, it means elements from the stack (which should be to the right)
    # are out of place.
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            right_boundary = max(right_boundary, stack.pop())
        stack.append(i)

    if right_boundary == -1:
        return 0  # Array is already sorted
    else:
        # The length is the distance between the boundaries plus one
        return right_boundary - left_boundary + 1


nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [1, 2, 3, 4]
# nums = [1]
# nums = [5, 4, 3, 2, 1]
# nums = [1, 3, 2, 2, 2]
# nums = [1, 2, 3, 3, 3]
print(findUnsortedSubarray(nums))
