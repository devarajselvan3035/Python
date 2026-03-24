"""
697. Degree of an Array
=======================
Guven a non-empty array of non-vegative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements:

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
"""

from typing import List


def findShortestSubArray(nums: List[int]) -> int:
    numsCount = {}
    degree = 0
    numsSeen = {}
    minLength = 0

    for idx, n in enumerate(nums):
        numsCount[n] = numsCount.setdefault(n, 0) + 1
        if n not in numsSeen:
            numsSeen[n] = idx

        if numsCount[n] > degree:
            degree = numsCount[n]
            minLength = idx - numsSeen[n] + 1

        elif numsCount[n] == degree:
            minLength = min(minLength, idx - numsSeen[n] + 1)

    return minLength


nums = [1, 2, 2, 3, 1]
# nums = [1, 2, 2, 3, 1, 4, 2]
print(findShortestSubArray(nums))
